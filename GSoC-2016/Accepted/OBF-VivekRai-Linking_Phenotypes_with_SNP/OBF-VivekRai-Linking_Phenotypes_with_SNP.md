# Linking Phenotypes to SNPs in openSNP

## Personal information

### Contact Information

* Student name: Vivek Rai
* Email(s): vivekraiiitkgp@gmail.com
* Skype: vivekrai.iitkgp
* Google+ (Hangouts): vivekraiiitkgp@gmail.com
* IRC: vivekrai @ freenode
* GitHub: https://github.com/vivekiitkgp
* Twitter: https://twitter.com/vivek_ziel

### Student affiliation

**Indian Institute of Technology Kharagpur**

*Integrated Dual Degree (Bachelor’s and Master’s)*

8th semester, 2017 (expected graduation)

### Brief bio

I am hooked to open-source software development, an ambitious outgrowth of my
personal interests to create [free](https://www.gnu.org/philosophy/free-sw.html)
(as in [freedom!](http://c2.com/cgi/wiki?FreeAsInBeer)) and
[open-source](http://c2.com/cgi/wiki?OpenSource) content.

* I like to [write](http://quora.com) and [read](https://vivekiitkgp.github.io/books.html).
* I love to [code](https://github.com/vivekiitkgp).
* I enjoy sharing my [experiences](https://vivekiitkgp.github.io).

These are my personal favorite projects that I have contributed to
significantly and learned a lot:

* [Sequenceserver](https://github.com/wurlmab/sequenceserver)
* [WIGI](https://github.com/notconfusing/WIGI) and [WIGI-website](https://github.com/hargup/WIGI-website)
* [Afra](https://github.com/wurlmab/afra)

I use [GNU/Linux](https://www.debian.org/releases/squeeze/i386/ch01s02.html.en)
(Ubuntu 14.04) with [awesome](https://awesome.naquadah.org/) window manager,
keep files under [version control](https://git-scm.com/), and edit using
[Vim](http://vim.org).

Further information and details of my general interests can be found on my
[blog](https://vivekiitkgp.github.io).

## Abstract

A crucial component of the openSNP infrastructure is to make the available data
more accessible to the general users and scientists alike. Currently, the portal
has independent listing of user *Phenotypes* and parsed *SNP*s. Each *SNP*s
entry have an additional information section where data from other credible
sources (PLoS, Mendeley, Genome.gov) is made available. There is, however, no
direct or inferred relationship available between the *SNP*s and the
corresponding *Phenotypes* (as reported). This document proposes to bridge the
connectivity between existing *Phenotypes* and genetic variants with the help of
already mined data and implementing additional services as necessary.

## Background

**OpenSNP** is a non-profit, open-source project founded on the principles of open
science and open data. The [free](https://en.wikipedia.org/wiki/Gratis_versus_libre) (as in free speech!) platform, since its
inception in 2011, has worked with a simple purpose of crowd-creating
a open-data resource by collecting personal genomics into the public domain. The
project, however, has no *traditional* academia support and is largely supported
by the project is developed and run by a group of citizen scientists, without
any attachment to a university or institution and without academic or large
industry funding. It won’t be exaggeration to say that it’s the contribution of
the volunteer community supported by decent infrastructure that in a span of
only five years the project has grown to over 5000 registered users.

It is only natural for the curators and the benefiting community to keep
improving upon the existing setup and scale up as per the requirements.
Currently, openSNP portal has a good database collection and shows mined
information in an easily searchable way. There is, however, a lot of scope in
improving the impact and reach of the project by modernizing the interface,
linking the databases and analysing the literature to allow for comprehensive
yet quick understanding.

This proposal seeks to work the latter problem of bridging different components
to allow for better interactivity and information conveyance.

## Project proposal

OpenSNP portal is based on general Model-View-Architecture (MVC) framework
provided by Ruby on Rails (or simply Rails).

Essentially, the different objectives (or components) are as follows:

### Backend

* **Database updates**: Since one SNP can have many phenotypes and vice-versa, there exists
    a many-to-many relationship between the two models.  Write database
    migration scripts (`db/migrate`) corresponding to above database schema
    changes.

    ```ruby
    +class CreateJoinTablePhenotypeSnp < ActiveRecord::Migration
    +  def self.up
    +    # see rails naming convention for naming JOIN tables
    +    create_table :phenotype_snps do |t|
    +      t.references :snp
    +      t.references :phenotype
    +      t.float :score
    +      t.timestamps
    +    end
    +  end
    +
    +  def self.down
    +    drop_table :phenotype_snps
    +  end
    +end
    ```

* **Updating models**: Update the database schema for both the models
* `models/snps.rb` and `models/phenotypes.rb`.

    ```ruby
    +class Snp < ActiveRecord::Base
    +  has_many :phenotype_snps
    +  has_many :phenotypes, through: :phenotype_snps

    +class Phenotype < ActiveRecord::Base
    +  has_many :phenotype_snps
    +  has_many :snps, through: :phenotype_snps
    ```

    Add new model `phenotype_snp.rb` describing the join table.

    ```ruby
    +class PhenotypeSnp < ActiveRecord::Base
    +  include PgSearchCommon
    +
    +  belongs_to :snp
    +  belongs_to :phenotype
    +end
    ```

* **Worker script**: Write worker script `snps_phenotype.rb` similar to `plos_search.rb` or
    `mendeley_search.rb`. The worker will query the database for
    records of the queried SNP, infer associations and update the database table
    `phenotype_snp`. This update process will be conservative in nature. That
    is, we could run it once using all the publications/phenotypes we already
    have and from there on only trigger updates when a) new phenotypes are
    entered, b) when new publications are entered. Both of these can lead to new
    associations.

    Currently, the literature/phenotype data is updated after one month, hence,
    `phenotype_snp` rows will be updated in same time-frame.

* **Update views**: The SNP views template will have an extra tab corresponding
    to the associated phenotypes. A typical relation table may look like:

    ```
    # (Rank) | ID | Phenotype name  | Users
    ---------------------------------------
    1        | 13 | Hair Color      | 599
    2        | 25 | Color Blindness | 441
    ```

    The table will show a **ranked** list of phenotypes along with the number of
    users who share the phenotype and the id of the phenotype.

    The corresponding modifications in `snps/show.html.erb` would be:

    ```html
    +  <li><a href="#phenotype">Phenotypes (<%= @snp.phenotype.count %>)</a></li>
    ..
    ..
    +  <div id="phenotype">
    +    <h3>Phenotypes related to this SNP</h3>
    +    <% if @snp.phenotypes.present? %>
    +      <table class="table table-striped" id="phenotypeTable">
    +        <thead>
    +          <tr>
    +            <th># (Rank)</th>
    +            <th>ID</th>
    +            <th>Phenotype name</th>
    +            <th># of users</th>
    +          </tr>
    +        </thead>
    +        <tbody>
    +          <% @snp.phenotypes.limit(100).each do |p|%>
    +            <tr>
    +              <td><%=PhenotypeSnp.where(snp_id: @snp.id).first.score%></td>
    +              <td><%=p.id%></td>
    +              <td><%=link_to(p.characteristic, p)%></td>
    +              <td><%=p.number_of_users%></td>
    +            </tr>
    +          <%end%>
    +        </tbody>
    +      </table>
    +    <% else %>
    +      We have not yet found any associated phenotypes.
    +    <% end %>
    +  </div>
    ```

    Similarly, we update the `phenotypes/show.html.erb` with a tab listing the
    associated SNPs.


* **Update controllers**: Once the models, view have been written, we update the
    `snps` and `phenotypes` controller to leverage the worker script and
    accordingly update the output `show`, `index` and `json` methods to return
    the updated results.

* **Populate database**: The worker scripts will be run separately as a `rake`
    task to populate the database based on already collect literature/phenotype
    information. No, API queries are made in this step.

    ```ruby
    namespace :custom do
      desc 'Adding custom data to Phenotype SNP table'
      task :snp_link => :environment do
        # test examples
        @snps = Snp.find_by_name('rs4475691')
        @phenotype = Phenotype.create :characteristic => 'Brown'
        PhenotypeSnp.create :snp => @snps, :phenotype => @phenotype, :score => 5

        @snps = Snp.find_by_name('rs3890745')
        @phenotype = Phenotype.create :characteristic => 'Height'
        PhenotypeSnp.create :snp => @snps, :phenotype => @phenotype, :score => 7
      end
    end
    ```

### Frontend

It would be interesting to showcase the resulting changes by including
informative visualizations on the front-end. However, since the portal
requires an user-interface update and migration to latest JavaScript and
Bootstrap framework, it would be wise to implement any visualizations in the
later part of the stage.

### Coding plan

In this section we discuss the algorithmic details of how to relate the SNPs to
their corresponding Phenotypes and a good way to rank them.

#### Inferring the phenotype

The initial approach could be to simply can for the phenotype keywords in the
literature data collected from Mendeley, PLoS, SNPedia and other resources.
Based on the hits obtained to these resources, a normalized score would be
generated which can be used to rank the phenotypes for a SNP.

#### Ranking the phenotypes

A first approach towards creating the association graph would be to rank the
phenotypes based on a simple *frequency lookup*. For each SNP in the database,
we find the frequency of occurrence of available phenotypes in the mined
literature from different sources. Since different sources have different
credibility, the score function will be a weighted sum of the counts from these
sources. For this, we can use the weights already used by openSNP.

That is, 5 for a count in SNPedia, 2 for PLoS, Genome.gov, or an annotation by
the Personal Genome Project, and 1 for an entry in Mendeley. Since the number of
hits for different sources can differ (say less results from SNPedia compared to
PLoS), the individual scores will be normalized by the number of results from
each source.

For example,

Score(SNP) = SUM [w(x)*count(x)/num_results(x)] / SUM [count(x)/num_total_results], where x in each source.

**Notes:**

* In subsequent refinements of this algorithm, we may wish to look for synonyms or
    recommendations from the recommendation system as well. That means that if
    a disease X is strongly related to a SNP Y, then it is quite likely that disease
    Y is also related.
* Using more data will also help us make better associations. For this, we may
    use the EMBL-EBI’s [Ensemble](http://ensembl.org/) [REST
    API](http://rest.ensembl.org/) to obtain direct phenotype data available
    from OMIM, ClinVar and other sources.

    For example,  a sample response from Ensemble’s API looks like:
    ```json
    {
      "most_severe_consequence": "missense_variant",
      ...
      "synonyms": [
        "306",
        "rs3182295",
        "rs386606420",
        "rs4714",
        "rs61617185",
        "rs17856353",
        "VAR_007096"
      ],
      ...
      "name": "rs699",
      "phenotypes": [
        {
          "study": "MIM:106150",
          "genes": "AGT",
          "trait": "HYPERTENSION, ESSENTIAL, SUSCEPTIBILITY TO",
          "risk_allele": "0001",
          "source": "OMIM",
          "variants": "rs699"
        },
        {
          "genes": "AGT",
          "trait": "Susceptibility to progression to renal failure in IgA nephropathy",
          "risk_allele": "G",
          "source": "ClinVar",
          "variants": null
        },
        {
          "genes": "AGT",
          "trait": "Preeclampsia, susceptibility to",
          "risk_allele": "G",
          "source": "ClinVar",
          "variants": null
        },
        {
          "genes": "AGT",
          "trait": "HYPERTENSION, ESSENTIAL, SUSCEPTIBILITY TO",
          "risk_allele": "G",
          "source": "ClinVar",
          "variants": null
        }
      ]
    }
    ```

    We can see that an additional `synonyms` key is available in the response
    that can also be used to eliminate result redundancy between the SNPs.

### Timeline (tentative)

*Through the coding period, emphasis is on creating well documented and tested
code. For this, one may commit frequently (with verbose messages), follow
a test-driven development style and use continuous integration services.*

**Community bonding period**

Spend time interacting with community members and learn more about openSNP and
its broader vision. The period can also be used to further refine, discuss and
plan the components of proposal which are not very clear.

Also, help plan out roadmap, create/fix minor issues and familiarize myself with
the codebase.

**Week 1 - Week 2**

* Set up [blog](https://vivekiitkgp.github.io/gsoc16) to document my progress
    through the project. An important component of openSNP project is to
    increase visibility and create impact. Writing short, introductory and
    useful posts detailing how to utilise data from openSNP for further analysis
    will be a great addition.
* Setup [code-climate](https://codeclimate.com/), [coverage](https://coveralls.io/).
* Integrate Rubocop in the travis-ci builds.
* Bi-weekly summary

**Week 3 - Week 4**

* Work on updating the database.
* Update models, write worker script.
* Bi-weekly summary

**Week 5 - Week 6**

* Thoroughly test the worker script, see if the implemented ranking algorithm
    shows reasonable accuracy.
* Update views, controllers and integrate with the user-interface
* Bi-weekly summary

*Mid term evaluations*

**Week 7 - Week 8**

* Populate database
* Test all the changes so far. If something is not working properly, fix it
    before moving on to other parts.
* Bi-weekly summary

**Week 9 - Week 10**

* Add front-end visualizations. The goal would be to write an independent
    visualization component that can be easily embedded in the web page. This can
    serve as a good example of how to consume data from the API.

* Bi-weekly summary

**Week 11 - Week 12**

*Week to scrub code, write tests, focus on documentation.*

*End term evaluations*

## Previous experience

Collaborator in many open-source projects. A few that I am personally fond of:

* [Sequenceserver](https://github.com/wurmlab/sequenceserver):  > 115+ commits,
    bioinformatics software, developed in Ruby, Frontend and backend design

* [Wikipedia Gender Indicators](https://github.com/hargup/WIGI-website):
  Wikimedia supported, developer and maintainer,
statistical analysis, visualization, used Python and JavaScript. See it in
[action](http://wigi.wmflabs.org).

* [Afra](https://github.com/yeban/Afra): JavaScript, Commits to improve the user
    interface.

These projects incorporated relevant development experience (unit testing,
coverage, code quality etc.) useful for this project.

Please see all my contributions at [GitHub](https://github.com/vivekiitkgp).
I also write occasionally at [shorts](https://vivekiitkgp.github.io).

## Mentors

Bastian Greshake, Philipp Bayer

