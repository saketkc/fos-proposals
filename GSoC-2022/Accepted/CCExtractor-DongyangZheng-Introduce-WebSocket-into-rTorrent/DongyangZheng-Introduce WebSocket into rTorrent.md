**Personal Information**
=====================
- Name: Dongyang Zheng
- Email: flash12561256@gmail.com
- Github: [Young-Flash](https://github.com/Young-Flash)
- Blog: [blog](https://young-flash.github.io/)
- Location: Guangzhou, China
- Time Zone: UTC+8
- University: South China Normal University
- Major: Computer Science And Technology

**Project Description**
=====================
- Name: [Implement a modern RPC interface for rTorrent](https://ccextractor.org/public/gsoc/rtorrent-modern-rpc/)
- Mentor: [@jesec](https://github.com/jesec)
- Goal:
  - **modernization**: implement JSON-RPC over WebSockets support on top of the
existing JSON-RPC over SCGI (raw socket) implementation, hook event emitting
function and send event to WebSocket subscribers.
  - **performance**: consider replacing the global lock with a shared lock.
  - **security**: TLS support.


**About me**
=====================
My major programming language is C++ and I really like it, I understand the syntax of C++, new features in modern C++, some knowledge about CMake and network programming over
TCP/IP, Websocket.

I have **open source experience**. I participated in a activity (named Summer 2021) similar to GSoC last summer and successfully passed the review of mentor and organizers. The project I am responsible for is to encapsulate the JDBC protocol for a graph database named Nebula Graph, it was done by me almost independently (of course, with the guidance of mentor), the
output (code and documentation) have been merged into official github repository. Now I am also a volunteer contributor in this open source community and continue to maintain this project. You can see the activity info [here](https://summer-ospp.ac.cn/2021/#/?lang=en) and my outcome can be seen [here](https://github.com/nebula-contrib/nebula-jdbc). I am in my master degree now, majoring computer science and technology in [Social Network Data Intelligence Lab](https://www.scholat.com/team/scholatteam), research area in Knowledge Graph, published a paper as the first author, more info about me can be seen [here](https://www.scholat.com/zhengdongyang).

**Homework**
=====================
- Build from source and run rTorrent, make dev environment and dependencies ready on my machine.
- Read source code in src/rpc and other parts related, understand the core concepts and RPC workflow
<img src="media/RPC workflow.png"/>

- Study the websocket protocol by [RFC6455](https://www.rfc-editor.org/rfc/rfc6455) and using the websocket framework, make a [quick demo](https://github.com/Young-Flash/websockets-demo) about how to use uWebsockets to implement a server which supports publish and subscribe over websockets protocol (with ssl).

- Accomplished qualification task posted by mentor, it's [here](https://github.com/Young-Flash/translator).
    - I implement a "translator", which takes JSON arguments from Websocket client, reformat it into SCGI and forward it to rTorrent, waiting response from rTorrent and then pass the response to the websocket client.
    - The core class design and data flow is shown below:
<img src="media/class design.png"/>

- **Add unix domain socket support for uWebSockets, it's [here](https://github.com/Young-Flash/uWebSockets).**

    - for uSockets: add interface `(LIBUS_SOCKET_DESCRIPTOR bsd_create_listen_socket_unix(const char *path, int options))` which takes the path to socket file as param to setup a listen socket.

    - for uWebSockets: add interface `(TemplatedApp &&listen_unix(std::string path, int options, MoveOnlyFunction<void(us_listen_socket_t *)> &&handler))` to support setup websocket server listening on socket file and set the permission of the socket file to 700 (S_IRWXU) defaultly

**Plan**
=====================

- Steps
  1. **for modernization**:

        introduce uWebsockets into the rTorrent to make client can communicate with rTorrent via websocket protocol, client can subscribe some specific topics, once the event occurs, server will push the notification to client automatically; implement some callback function and bind to the events we care about, execute them when event occurs.

  2. **for security**:

        upgrade ws (websocket) to wss (websocket with TLS), specifies the path of ssl credential in the config file of rTorrent, when the program launch, load the credential to init a wss connection
  3. **for performance**:

        it is about the global lock (a static member (std::mutex) in the class torrent::thread_base), the global lock is not used to interrupt the RPC routines rather the "main_thread", maybe need to modify the code in libtorrent (kind of tricky, leave it for future consideration).

- 3rd party libraries: [uWebSockets](https://github.com/uNetworking/uWebSockets) (Apache License 2.0) or [libwebsockets](https://github.com/warmcat/libwebsockets) (MIT license)
  
- Support I need from community:: discuss with mentor in case of query.

**Timeline**
=====================

## official overview

- **May 20**: accepted GSoC contributor projects announced;
- **May 21: - June 12**: community Bonding Period | GSoC contributors get to know mentors, read documentation, get up to speed to begin working on their projects;
- **June 13 - July 25**: coding officially begins;
- **July 26 - September 4**: work Period | GSoC contributors work on their project with guidance from Mentors;
- **September 5 - September 12**: final week.

## details

- **before May 20**
  - communicate with mentor to understand and details the goal of project;
  - get familiar with the websocket protocol, make a demo [here](https://github.com/Young-Flash/websockets-demo);
  - get the [qualification task](https://github.com/Young-Flash/translator) done.

- **May 21 - June 12**
  - clarify the RPC call process in details, replace SCGI routine with websocket in a thread; first make it work under tcp ip:port, then consider to add unix domain socket support
  - test the connection between rTorrent and websocket client (by [Postman](https://www.postman.com/))

- **June 13 - July 25**
  - implement "server push" capacity: design some callback function (notify client) to execute automatically when events happens (download state changes, etc), **current idea**: when the state of a torrent changes, `DL_TRIGGER_EVENT(download, event_name)` will be called, so we can hook event emitting here according to the parameter "event_name".
  - Take `event.download.finished` as example, when this event happens, websocket routine will send message below to client:
    ```json
    {
        "id":null,
        "jsonrpc":"2.0",
        "result":[
            {
                "torrent_hash_value":"F243DA99EB8A210A5B8AC480878B4564DF6BE221",
                "state":"finished",
                "time_stamp":1649656905
            }
        ]
    }
    ```
  - prepare for phase 1 evaluation

- **July 26 - August 4**
    - buffer week for any unpredictable problems

- **August 5 - September 4**
    - consider to add unix domain socket support for uWebsockets / uSockets, this may challenging as it not merely to set `AF_LOCAL` when socket setup, but need to consider both configuration and API compatibility. This work achieved initial progress, I will try to make a [PR](https://github.com/uNetworking/uWebSockets/pull/1486) to uWebSockets, other features should be add such as make it compiles on Windows, client connection function and benchmark, etc
    - try to reduce the granularity of lock in libtorrent;
    - prepare for the final evaluation

- **September 5 - September 12**
  - code style and quality review, dev documentation
  - prepare for final evaluation

**Why me**
=====================
I like modern C++ and the project was written in C++ 17, I also interested in network programming and the project requires websocket and RPC. I think my technology stack matches the requirements of this project. When I find this project and make some research on it (build and run rTorrent and read the source code of it, communicate with mentor about project requirements and details), I make a decision that all in this one and leave others for no consideration, this is also my usual style of doing things, making decisions after research and focusing on it attentively.

I love the way open source works, and participating in open Source activities has introduced me to things I'd never known before, improved my coding skills and met a lot of interesting people who I've enjoyed communicating with, and I hope to contribute more to the open source world. I first got involved with open source at Summer 2021 (mentioned above) last year, but my open source experience didn't end with the end of the activity, now I am a volunteer contributor in the Nebula Graph community, maintaining on the projects I was previously working on. If I'm lucky enough to be selected for this project, I'll take it seriously, keep contributing to the community by continuing to maintain it in the future. Although GSoC 2022 may be over, my enthusiasm for open source isn't.