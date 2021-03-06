#A Bittorrent Client using Python and Twisted#

This project was written to create a client implementing the
Bittorrent Protocol. It was an interesting way to learn about
implementing a message passing project from a spec. More about
the steps in the project and how to create your own can be found
in my blog post here:
www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-1/
(and at ...-part-2)

##Learning##
1. Understanding a spec and how to implement it.
2. Event-driven programming concepts using Twisted. Multiple peer
    connections handled at once. Multiple torrents can be downloaded
    at once as well.
3. OOP principles in python, esp dealing with multiple classes and files.
4. Python modules: structs, bencode, bitstring, hashlib, requests,
    os, and time.

##To Use:##
1. Clone repo.
2. Ensure you have all needed external python libraries.
3. Update the torrent_client.ini file to include any torrent files
    you wish to download and the folder to download them to.
4. On command-line: python active_torrent.py

##Notes:##
This client is not perfect/finished. I plan to implement more 
functionality in the future. In particular:
- it does not upload files to peers, only downloads
- once peer connections are lost (due to closed connections or something
    else), they cannot be restarted. The client can only ever use the peers
    it starts with. The effect of this is that very large files with
    few peers may not be downloadable wtih this client as it is currently
    implemented.
- no Cancel messages are currently sent when pieces requested multiple
    times are received. No Have messages sent either since not serving
    files.
