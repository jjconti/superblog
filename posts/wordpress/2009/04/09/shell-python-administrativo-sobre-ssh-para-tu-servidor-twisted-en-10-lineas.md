<html><body><p>entre tu reactor.listeTCP(puerto, factory) y reactor.run():

</p><pre>from twisted.conch import manhole, manhole_ssh

from twisted.cred import portal, checkers 



def getManholeFactory(namespace, **passwords):

    realm = manhole_ssh.TerminalRealm()

    def getManhole(_): return manhole.Manhole(namespace)

    realm.chainedProtocolFactory.protocolFactory = getManhole

    p = portal.Portal(realm)

    p.registerChecker(

    checkers.InMemoryUsernamePasswordDatabaseDontUse(**passwords))

    f = manhole_ssh.ConchFactory(p)

    return f



reactor.listenTCP(2222, getManholeFactory(globals(), admin='aaa'))</pre>

Los aplausos para <a href="http://www.devshed.com/c/a/Python/SSH-with-Twisted/3/" target="_blank">este tutorial</a>.</body></html>