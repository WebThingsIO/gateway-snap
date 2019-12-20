from snapcraft.plugins.nodejs import NodePlugin
import os


class BetterNodePlugin(NodePlugin):

    def pull(self):
        """
        Why exactly are we overriding the pull stage of this plugin?

        Well... the official nodejs plugin is wrong and tries to do an
        `npm install` during the pull phase, before dependencies are even
        installed. Makes sense, right?

        So, instead, let's just do the right thing here.
        """
        os.makedirs(self._npm_dir, exist_ok=True)
        self._nodejs_tar.download()
        self._nodejs_tar.provision(self._npm_dir, clean_target=False, keep_tarball=True)
