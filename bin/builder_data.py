"""
This file specifies the build targets and dependencies for all
automatically generated makefiles used to generate the MongoDB
documentation.

Scripts named ``makefile_builder_<name>.py`` actually generates the
makefile, which is in turn, included in the project's main makefile,
where the following makefile instructions are responsible for
(re)generating and integrating these makefiles:

.. code-block:: makefile

   -include $(output)/makefile.pdfs
   -include $(output)/makefile.links
   -include $(output)/makefile.sphinx
   -include $(output)/makefile.releases
   -include $(output)/makefile.errors
   -include $(output)/makefile.migrations

   $(output)/makefile.%:bin/makefile-builder/%.py bin/makefile_builder.py bin/builder_data.py
        @$(PYTHONBIN) bin/makefile-builder/$(subst .,,$(suffix $@)).py $@

These ``makefile_builder_<name>.py`` scripts use the
``MakefileBuilder`` class from the ``makefile_builder.py``script to
simplify make syntax and make the build process more obvious. You can
inspect these scripts directly view their output as needed to
understand their operation.

If you need to add a new target to the build produced by one of the
existing scripts, see the comments in this file. Typically, you only
need to add a tuple to the appropriate lists, which contains
information about the build target, and the block of the makefile,
which (can) control how ``MakefileBuilder`` orders sections of the
makefile, although as of launch, no builders use this feature.
"""

links = [
# The elements of the tuples in the ``links`` list are:
#     0. ``make_target``: the name of the target,
#     1. ``link_target``: the name of the file the symlink should point
#        at.
#     2. ``makefile_block``: the block of the makefile that captures
#        the kind/purpose of link. If the type of the build is
#        "content," the link is not a PHONY make target.
#
#    (make_target, link_target, makefile_block),
     ('$(public-output)/manual', '$(manual-branch)', 'structural'),
     ('$(public-branch-output)/MongoDB-Manual.epub', 'MongoDB-Manual-$(current-branch).epub', 'content'),
     ('$(public-branch-output)/tutorials', 'tutorial', 'use'),
     ('$(public-branch-output)/reference/methods', 'method', 'use'),
     ('$(public-branch-output)/reference/method/reIndex', 'db.collection.reIndex', 'redirect'),
     ('$(public-branch-output)/reference/operator/atomic', 'isolated', 'redirect'),
     ('$(public-branch-output)/reference/mongo-shell-reference', 'mongo-shell', 'redirect'),
     ('$(public-branch-output)/reference/method/getShardDistribution', 'db.collection.getShardDistribution', 'redirect'),
     ('$(public-branch-output)/reference/method/Mongo.getDB', 'getDB', 'redirect'),
     ('$(public-branch-output)/reference/method/getShardVersion', 'db.collection.getShardVersion', 'redirect'),
     ('$(public-branch-output)/reference/command/whatsMyUri', 'whatsmyuri', 'redirect'),
     ('$(public-branch-output)/reference/command/writeBackListen', 'writebacklisten', 'redirect'),
     ('$(public-branch-output)/reference/command/isdbGrid', 'isdbgrid', 'redirect'),
     ('$(public-branch-output)/reference/command/emptyCapped', 'emptycapped', 'redirect'),
     ('$(public-branch-output)/reference/command/printShardingStatus', '../method/db.printShardingStatus', 'redirect'),
     ('$(public-branch-output)/administration/sharding-architectures', 'sharded-cluster-architectures', 'redirect'),
     ('$(public-branch-output)/administration/replication-architectures', 'replica-set-architectures', 'redirect'),
     ('$(public-branch-output)/administration/sharding', 'sharded-clusters', 'redirect'),
     ('$(public-branch-output)/core/sharding', 'sharded-clusters', 'redirect'),
     ('$(public-branch-output)/core/sharding-internals', 'sharded-cluster-internals', 'redirect'),
     ('$(public-branch-output)/tutorial/install-mongodb-on-redhat-centos-or-fedora-linux', 'install-mongodb-on-red-hat-centos-or-fedora-linux', 'redirect'),
]

pdfs = [
# The elements of the tuples in the ``pdfs`` list are:
#     0. ``root-name``: the name of the file, without extension, that
#        Sphinx generates.
#     1. ``tag`` the tag on the file name, used in the PDF provided to
#        users.
#
#   (root-name, tag),
    ('MongoDB', 'Manual'),
    ('MongoDB-reference', 'manual'),
    ('MongoDB-use-cases', 'guide'),
    ('MongoDB-crud', 'guide'),
]

# The elements in the ``texinfo`` list are the texinfo filenames generated by Sphinx.
texinfo = [ 'mongodb-reference', 'mongodb-crud', 'mongodb-manual' ]

sphinx = [
# The items in the ``sphinx`` list are the name of the sphinx builder.
#
    'dirhtml',
    'singlehtml',
    'latex',
    'epub',
    'html',
    'gettext',
    'man',
    'json',
    'changes',
    'doctest',
    'linkcheck',
    'texinfo',
    'draft-html',
    'draft-latex',
]

install_guides = [
# The elements of the tuples in ``install_guides`` list are:
#     0. The ``target`` to build. Includes both install guides and the
#        source files with the curl commands.
#     1. The ``dependency`` of the build. Is ``None`` if this is a
#        source file.
#
#   (target, dep),
    ('source/tutorial/install-mongodb-on-linux.txt', 'source/includes/install-curl-release-linux-64.rst source/includes/install-curl-release-linux-32.rst'),
    ('source/tutorial/install-mongodb-on-os-x.txt', 'source/includes/install-curl-release-osx-64.rst'),
    ('linux-64', None),
    ('linux-32', None),
    ('osx-64', None),
]

# The elements of the ``error_pages`` list correspond to the file
# names of each error page, and their HTTP error code.
error_pages = [ '401', '403', '404', '410' ]

migrations = [
# The elements of the tuples in the ``migrations`` list are:
#     0. ``target``: the name of the target, to migrate a file to.
#     1. ``source``: the name of the source file to migrate the file
#        from.
#     2. ``makefile_block``: the block of the makefile that captures
#        the kind/purpose of the migration.
#
#   ('target', 'source', 'block'),
    ('$(public-output)/index.html', 'themes/docs.mongodb.org/index.html', 'static'),
    ('$(public-output)/sitemap.xml', 'themes/docs.mongodb.org/sitemap.xml', 'static'),
    ('$(public-output)/10gen-gpg-key.asc', 'themes/docs.mongodb.org/10gen-gpg-key.asc', 'static'),
    ('$(public-output)/10gen-security-gpg-key.asc', 'themes/docs.mongodb.org/10gen-security-gpg-key.asc', 'static'),
    ('$(public-output)/osd.xml', 'themes/docs.mongodb.org/osd.xml', 'access'),
    ('$(public-branch-output)/sitemap.xml.gz', '$(output)/sitemap.xml.gz', 'access'),
    ('$(public-branch-output)/.htaccess', 'themes/docs.mongodb.org/.htaccess', 'access'),
    ('$(public-branch-output)/single/search.html', '$(branch-output)/dirhtml/search/index.html', 'content'),
    ('$(public-branch-output)/MongoDB-Manual-$(current-branch).epub', '$(branch-output)/epub/MongoDB.epub', 'content'),
    ('$(branch-output)/epub/MongoDB.epub','$(branch-output)/epub/mongodb-manual.epub', 'content'),
]

sphinx_migrations = [
# The elements of the tuples in the ``sphinx_migrations`` list are:
#     0. ``target``: the name of the target.
#     1. ``dependency``: the name of the dependency. ``None`` is
#        acceptable.
#
#   (target, dependency),
    ('source/about.txt', None),
    ('$(branch-output)/dirhtml', 'dirhtml'),
    ('$(branch-output)/html', 'html'),
    ('$(branch-output)/singlehtml', 'singlehtml')
]
