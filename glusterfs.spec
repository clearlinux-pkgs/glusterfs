#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glusterfs
Version  : 4.0.1
Release  : 9
URL      : https://download.gluster.org/pub/gluster/glusterfs/LATEST/glusterfs-4.0.1.tar.gz
Source0  : https://download.gluster.org/pub/gluster/glusterfs/LATEST/glusterfs-4.0.1.tar.gz
Summary  : Distributed File System
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: glusterfs-bin
Requires: glusterfs-legacypython
Requires: glusterfs-config
Requires: glusterfs-lib
Requires: glusterfs-doc
Requires: glusterfs-data
Requires: glusterfs-python
BuildRequires : acl-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : fuse-dev
BuildRequires : libaio-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(liburcu-bp)
BuildRequires : pkgconfig(liburcu-cds)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)

BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : xz-dev
Patch1: build.patch

%description
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package includes the glusterfs binary, the glusterfsd daemon and the
libglusterfs and glusterfs translator modules common to both GlusterFS server
and client framework.

%package bin
Summary: bin components for the glusterfs package.
Group: Binaries
Requires: glusterfs-data
Requires: glusterfs-config

%description bin
bin components for the glusterfs package.


%package config
Summary: config components for the glusterfs package.
Group: Default

%description config
config components for the glusterfs package.


%package data
Summary: data components for the glusterfs package.
Group: Data

%description data
data components for the glusterfs package.


%package dev
Summary: dev components for the glusterfs package.
Group: Development
Requires: glusterfs-lib
Requires: glusterfs-bin
Requires: glusterfs-data
Provides: glusterfs-devel

%description dev
dev components for the glusterfs package.


%package doc
Summary: doc components for the glusterfs package.
Group: Documentation

%description doc
doc components for the glusterfs package.


%package legacypython
Summary: legacypython components for the glusterfs package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the glusterfs package.


%package lib
Summary: lib components for the glusterfs package.
Group: Libraries
Requires: glusterfs-data

%description lib
lib components for the glusterfs package.


%package python
Summary: python components for the glusterfs package.
Group: Default

%description python
python components for the glusterfs package.


%prep
%setup -q -n glusterfs-4.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522512661
%configure --disable-static --localstatedir=/usr/share/glusterfs PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522512661
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/ocf/resource.d/glusterfs/glusterd
/usr/lib/ocf/resource.d/glusterfs/volume
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/__pycache__/debug-trace.cpython-36.pyc
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/debug-trace.py
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/debug-trace.pyc
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/helloworld.py
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/helloworld.pyc
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/negative.py
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy/negative.pyc

%files bin
%defattr(-,root,root,-)
/usr/bin/conf.py
/usr/bin/fusermount-glusterfs
/usr/bin/gcron.py
/usr/bin/gf_attach
/usr/bin/gfind_missing_files
/usr/bin/glfsheal
/usr/bin/gluster
/usr/bin/gluster-eventsapi
/usr/bin/gluster-georep-sshkey
/usr/bin/gluster-mountbroker
/usr/bin/gluster-setgfid2path
/usr/bin/glusterd
/usr/bin/glustereventsd
/usr/bin/glusterfind
/usr/bin/glusterfs
/usr/bin/glusterfsd
/usr/bin/mount.glusterfs
/usr/bin/snap_scheduler.py
/usr/libexec/glusterfs/__pycache__/peer_eventsapi.cpython-36.pyc
/usr/libexec/glusterfs/__pycache__/peer_georep-sshkey.cpython-36.pyc
/usr/libexec/glusterfs/__pycache__/peer_mountbroker.cpython-36.pyc
/usr/libexec/glusterfs/events/__init__.py
/usr/libexec/glusterfs/events/__init__.pyc
/usr/libexec/glusterfs/events/__pycache__/__init__.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/eventsapiconf.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/eventtypes.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/gf_event.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/glustereventsd.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/handlers.cpython-36.pyc
/usr/libexec/glusterfs/events/__pycache__/utils.cpython-36.pyc
/usr/libexec/glusterfs/events/eventsapiconf.py
/usr/libexec/glusterfs/events/eventsapiconf.pyc
/usr/libexec/glusterfs/events/eventtypes.py
/usr/libexec/glusterfs/events/eventtypes.pyc
/usr/libexec/glusterfs/events/gf_event.py
/usr/libexec/glusterfs/events/gf_event.pyc
/usr/libexec/glusterfs/events/glustereventsd.py
/usr/libexec/glusterfs/events/handlers.py
/usr/libexec/glusterfs/events/handlers.pyc
/usr/libexec/glusterfs/events/utils.py
/usr/libexec/glusterfs/events/utils.pyc
/usr/libexec/glusterfs/gfind_missing_files/__pycache__/gfid_to_path.cpython-36.pyc
/usr/libexec/glusterfs/gfind_missing_files/gcrawler
/usr/libexec/glusterfs/gfind_missing_files/gfid_to_path.py
/usr/libexec/glusterfs/gfind_missing_files/gfid_to_path.sh
/usr/libexec/glusterfs/gfind_missing_files/gfind_missing_files.sh
/usr/libexec/glusterfs/glusterfind/S57glusterfind-delete-post.py
/usr/libexec/glusterfs/glusterfind/__init__.py
/usr/libexec/glusterfs/glusterfind/__init__.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/S57glusterfind-delete-post.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/__init__.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/brickfind.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/changelog.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/changelogdata.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/conf.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/libgfchangelog.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/main.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/nodeagent.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/__pycache__/utils.cpython-36.pyc
/usr/libexec/glusterfs/glusterfind/brickfind.py
/usr/libexec/glusterfs/glusterfind/changelog.py
/usr/libexec/glusterfs/glusterfind/changelogdata.py
/usr/libexec/glusterfs/glusterfind/changelogdata.pyc
/usr/libexec/glusterfs/glusterfind/conf.py
/usr/libexec/glusterfs/glusterfind/conf.pyc
/usr/libexec/glusterfs/glusterfind/libgfchangelog.py
/usr/libexec/glusterfs/glusterfind/libgfchangelog.pyc
/usr/libexec/glusterfs/glusterfind/main.py
/usr/libexec/glusterfs/glusterfind/main.pyc
/usr/libexec/glusterfs/glusterfind/nodeagent.py
/usr/libexec/glusterfs/glusterfind/tool.conf
/usr/libexec/glusterfs/glusterfind/utils.py
/usr/libexec/glusterfs/glusterfind/utils.pyc
/usr/libexec/glusterfs/gsyncd
/usr/libexec/glusterfs/gverify.sh
/usr/libexec/glusterfs/mount-shared-storage.sh
/usr/libexec/glusterfs/peer_add_secret_pub
/usr/libexec/glusterfs/peer_eventsapi.py
/usr/libexec/glusterfs/peer_georep-sshkey.py
/usr/libexec/glusterfs/peer_gsec_create
/usr/libexec/glusterfs/peer_mountbroker
/usr/libexec/glusterfs/peer_mountbroker.py
/usr/libexec/glusterfs/python/syncdaemon/README.md
/usr/libexec/glusterfs/python/syncdaemon/__init__.py
/usr/libexec/glusterfs/python/syncdaemon/__init__.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/__init__.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/argsupgrade.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/changelogagent.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/conf.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/gsyncd.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/gsyncdconfig.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/libcxattr.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/libgfchangelog.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/logutils.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/monitor.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/rconf.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/repce.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/resource.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/subcmds.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/__pycache__/syncdutils.cpython-36.pyc
/usr/libexec/glusterfs/python/syncdaemon/argsupgrade.py
/usr/libexec/glusterfs/python/syncdaemon/argsupgrade.pyc
/usr/libexec/glusterfs/python/syncdaemon/changelogagent.py
/usr/libexec/glusterfs/python/syncdaemon/changelogagent.pyc
/usr/libexec/glusterfs/python/syncdaemon/conf.py
/usr/libexec/glusterfs/python/syncdaemon/conf.pyc
/usr/libexec/glusterfs/python/syncdaemon/gsyncd.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncd.pyc
/usr/libexec/glusterfs/python/syncdaemon/gsyncdconfig.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncdconfig.pyc
/usr/libexec/glusterfs/python/syncdaemon/gsyncdstatus.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncdstatus.pyc
/usr/libexec/glusterfs/python/syncdaemon/ipaddr.py
/usr/libexec/glusterfs/python/syncdaemon/ipaddr.pyc
/usr/libexec/glusterfs/python/syncdaemon/libcxattr.py
/usr/libexec/glusterfs/python/syncdaemon/libcxattr.pyc
/usr/libexec/glusterfs/python/syncdaemon/libgfchangelog.py
/usr/libexec/glusterfs/python/syncdaemon/libgfchangelog.pyc
/usr/libexec/glusterfs/python/syncdaemon/logutils.py
/usr/libexec/glusterfs/python/syncdaemon/logutils.pyc
/usr/libexec/glusterfs/python/syncdaemon/master.py
/usr/libexec/glusterfs/python/syncdaemon/master.pyc
/usr/libexec/glusterfs/python/syncdaemon/monitor.py
/usr/libexec/glusterfs/python/syncdaemon/monitor.pyc
/usr/libexec/glusterfs/python/syncdaemon/rconf.py
/usr/libexec/glusterfs/python/syncdaemon/rconf.pyc
/usr/libexec/glusterfs/python/syncdaemon/repce.py
/usr/libexec/glusterfs/python/syncdaemon/repce.pyc
/usr/libexec/glusterfs/python/syncdaemon/resource.py
/usr/libexec/glusterfs/python/syncdaemon/resource.pyc
/usr/libexec/glusterfs/python/syncdaemon/subcmds.py
/usr/libexec/glusterfs/python/syncdaemon/subcmds.pyc
/usr/libexec/glusterfs/python/syncdaemon/syncdutils.py
/usr/libexec/glusterfs/python/syncdaemon/syncdutils.pyc
/usr/libexec/glusterfs/set_geo_rep_pem_keys.sh

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/glusterd.service
/usr/lib/systemd/system/glustereventsd.service
/usr/lib/systemd/system/glusterfssharedstorage.service

%files data
%defattr(-,root,root,-)
/usr/share/glusterfs/lib/glusterd/groups/gluster-block
/usr/share/glusterfs/lib/glusterd/groups/metadata-cache
/usr/share/glusterfs/lib/glusterd/groups/nl-cache
/usr/share/glusterfs/lib/glusterd/groups/virt
/usr/share/glusterfs/lib/glusterd/hooks/1/add-brick/post/disabled-quota-root-xattr-heal.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/add-brick/pre/S28Quota-enable-root-xattr-heal.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/create/post/S10selinux-label-brick.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/delete/post/S57glusterfind-delete-post
/usr/share/glusterfs/lib/glusterd/hooks/1/delete/pre/S10selinux-del-fcontext.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/gsync-create/post/S56glusterd-geo-rep-create-post.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/set/post/S30samba-set.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/set/post/S32gluster_enable_shared_storage.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/start/post/S29CTDBsetup.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/start/post/S30samba-start.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/stop/pre/S29CTDB-teardown.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/stop/pre/S30samba-stop.sh
/usr/share/glusterfs/scripts/__pycache__/eventsdash.cpython-36.pyc
/usr/share/glusterfs/scripts/__pycache__/schedule_georep.cpython-36.pyc
/usr/share/glusterfs/scripts/control-cpu-load.sh
/usr/share/glusterfs/scripts/control-mem.sh
/usr/share/glusterfs/scripts/eventsdash.py
/usr/share/glusterfs/scripts/generate-gfid-file.sh
/usr/share/glusterfs/scripts/get-gfid.sh
/usr/share/glusterfs/scripts/gsync-sync-gfid
/usr/share/glusterfs/scripts/gsync-upgrade.sh
/usr/share/glusterfs/scripts/post-upgrade-script-for-quota.sh
/usr/share/glusterfs/scripts/pre-upgrade-script-for-quota.sh
/usr/share/glusterfs/scripts/schedule_georep.py
/usr/share/glusterfs/scripts/slave-upgrade.sh
/usr/share/glusterfs/scripts/stop-all-gluster-processes.sh

%files dev
%defattr(-,root,root,-)
/usr/include/glusterfs/api/glfs-handles.h
/usr/include/glusterfs/api/glfs.h
/usr/include/glusterfs/atomic.h
/usr/include/glusterfs/byte-order.h
/usr/include/glusterfs/call-stub.h
/usr/include/glusterfs/checksum.h
/usr/include/glusterfs/circ-buff.h
/usr/include/glusterfs/client_t.h
/usr/include/glusterfs/cluster-syncop.h
/usr/include/glusterfs/common-utils.h
/usr/include/glusterfs/compat-errno.h
/usr/include/glusterfs/compat-uuid.h
/usr/include/glusterfs/compat.h
/usr/include/glusterfs/compound-fop-utils.h
/usr/include/glusterfs/daemon.h
/usr/include/glusterfs/default-args.h
/usr/include/glusterfs/defaults.h
/usr/include/glusterfs/dict.h
/usr/include/glusterfs/event-history.h
/usr/include/glusterfs/event.h
/usr/include/glusterfs/events.h
/usr/include/glusterfs/fd-lk.h
/usr/include/glusterfs/fd.h
/usr/include/glusterfs/gf-dirent.h
/usr/include/glusterfs/gfchangelog/changelog.h
/usr/include/glusterfs/gfdb/gfdb_data_store.h
/usr/include/glusterfs/gfdb/gfdb_data_store_helper.h
/usr/include/glusterfs/gfdb/gfdb_data_store_types.h
/usr/include/glusterfs/gfdb/gfdb_mem-types.h
/usr/include/glusterfs/gfdb/gfdb_sqlite3.h
/usr/include/glusterfs/gfdb/gfdb_sqlite3_helper.h
/usr/include/glusterfs/gidcache.h
/usr/include/glusterfs/glfs-message-id.h
/usr/include/glusterfs/globals.h
/usr/include/glusterfs/glusterfs-acl.h
/usr/include/glusterfs/glusterfs.h
/usr/include/glusterfs/graph-utils.h
/usr/include/glusterfs/hashfn.h
/usr/include/glusterfs/iatt.h
/usr/include/glusterfs/inode.h
/usr/include/glusterfs/iobuf.h
/usr/include/glusterfs/latency.h
/usr/include/glusterfs/libglusterfs-messages.h
/usr/include/glusterfs/list.h
/usr/include/glusterfs/lkowner.h
/usr/include/glusterfs/locking.h
/usr/include/glusterfs/logging.h
/usr/include/glusterfs/lvm-defaults.h
/usr/include/glusterfs/mem-pool.h
/usr/include/glusterfs/mem-types.h
/usr/include/glusterfs/monitoring.h
/usr/include/glusterfs/options.h
/usr/include/glusterfs/parse-utils.h
/usr/include/glusterfs/protocol-common.h
/usr/include/glusterfs/quota-common-utils.h
/usr/include/glusterfs/rbthash.h
/usr/include/glusterfs/refcount.h
/usr/include/glusterfs/revision.h
/usr/include/glusterfs/rot-buffs.h
/usr/include/glusterfs/rpc/acl3-xdr.h
/usr/include/glusterfs/rpc/changelog-xdr.h
/usr/include/glusterfs/rpc/cli1-xdr.h
/usr/include/glusterfs/rpc/glusterd1-xdr.h
/usr/include/glusterfs/rpc/glusterfs-fops.h
/usr/include/glusterfs/rpc/glusterfs3-xdr.h
/usr/include/glusterfs/rpc/glusterfs3.h
/usr/include/glusterfs/rpc/glusterfs4-xdr.h
/usr/include/glusterfs/rpc/mount3udp.h
/usr/include/glusterfs/rpc/msg-nfs3.h
/usr/include/glusterfs/rpc/nlm4-xdr.h
/usr/include/glusterfs/rpc/nsm-xdr.h
/usr/include/glusterfs/rpc/portmap-xdr.h
/usr/include/glusterfs/rpc/protocol-common.h
/usr/include/glusterfs/rpc/rpc-clnt-ping.h
/usr/include/glusterfs/rpc/rpc-clnt.h
/usr/include/glusterfs/rpc/rpc-common-xdr.h
/usr/include/glusterfs/rpc/rpc-drc.h
/usr/include/glusterfs/rpc/rpc-lib-messages.h
/usr/include/glusterfs/rpc/rpc-pragmas.h
/usr/include/glusterfs/rpc/rpc-transport.h
/usr/include/glusterfs/rpc/rpcsvc-common.h
/usr/include/glusterfs/rpc/rpcsvc.h
/usr/include/glusterfs/rpc/xdr-common.h
/usr/include/glusterfs/rpc/xdr-generic.h
/usr/include/glusterfs/rpc/xdr-nfs3.h
/usr/include/glusterfs/rpc/xdr-rpc.h
/usr/include/glusterfs/rpc/xdr-rpcclnt.h
/usr/include/glusterfs/run.h
/usr/include/glusterfs/server/authenticate.h
/usr/include/glusterfs/server/server-common.h
/usr/include/glusterfs/server/server-helpers.h
/usr/include/glusterfs/server/server-mem-types.h
/usr/include/glusterfs/server/server-messages.h
/usr/include/glusterfs/server/server.h
/usr/include/glusterfs/stack.h
/usr/include/glusterfs/statedump.h
/usr/include/glusterfs/store.h
/usr/include/glusterfs/strfd.h
/usr/include/glusterfs/syncop-utils.h
/usr/include/glusterfs/syncop.h
/usr/include/glusterfs/syscall.h
/usr/include/glusterfs/template-component-messages.h
/usr/include/glusterfs/throttle-tbf.h
/usr/include/glusterfs/timer.h
/usr/include/glusterfs/timespec.h
/usr/include/glusterfs/trie.h
/usr/include/glusterfs/upcall-utils.h
/usr/include/glusterfs/xlator.h
/usr/include/glusterfs/y.tab.h
/usr/lib64/libgfapi.so
/usr/lib64/libgfchangelog.so
/usr/lib64/libgfdb.so
/usr/lib64/libgfrpc.so
/usr/lib64/libgfxdr.so
/usr/lib64/libglusterfs.so
/usr/lib64/pkgconfig/glusterfs-api.pc
/usr/lib64/pkgconfig/libgfchangelog.pc
/usr/lib64/pkgconfig/libgfdb.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/glusterfs/*
%doc /usr/share/man/man8/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/glusterfs/4.0.1/auth/addr.so
/usr/lib64/glusterfs/4.0.1/auth/login.so
/usr/lib64/glusterfs/4.0.1/rpc-transport/socket.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/afr.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/dht.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/disperse.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/distribute.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/ec.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/nufa.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/replicate.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/stripe.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/switch.so
/usr/lib64/glusterfs/4.0.1/xlator/cluster/tier.so
/usr/lib64/glusterfs/4.0.1/xlator/debug/delay-gen.so
/usr/lib64/glusterfs/4.0.1/xlator/debug/error-gen.so
/usr/lib64/glusterfs/4.0.1/xlator/debug/io-stats.so
/usr/lib64/glusterfs/4.0.1/xlator/debug/sink.so
/usr/lib64/glusterfs/4.0.1/xlator/debug/trace.so
/usr/lib64/glusterfs/4.0.1/xlator/encryption/crypt.so
/usr/lib64/glusterfs/4.0.1/xlator/encryption/rot-13.so
/usr/lib64/glusterfs/4.0.1/xlator/features/access-control.so
/usr/lib64/glusterfs/4.0.1/xlator/features/arbiter.so
/usr/lib64/glusterfs/4.0.1/xlator/features/barrier.so
/usr/lib64/glusterfs/4.0.1/xlator/features/bit-rot.so
/usr/lib64/glusterfs/4.0.1/xlator/features/bitrot-stub.so
/usr/lib64/glusterfs/4.0.1/xlator/features/cdc.so
/usr/lib64/glusterfs/4.0.1/xlator/features/changelog.so
/usr/lib64/glusterfs/4.0.1/xlator/features/changetimerecorder.so
/usr/lib64/glusterfs/4.0.1/xlator/features/gfid-access.so
/usr/lib64/glusterfs/4.0.1/xlator/features/glupy.so
/usr/lib64/glusterfs/4.0.1/xlator/features/index.so
/usr/lib64/glusterfs/4.0.1/xlator/features/leases.so
/usr/lib64/glusterfs/4.0.1/xlator/features/locks.so
/usr/lib64/glusterfs/4.0.1/xlator/features/marker.so
/usr/lib64/glusterfs/4.0.1/xlator/features/posix-locks.so
/usr/lib64/glusterfs/4.0.1/xlator/features/quiesce.so
/usr/lib64/glusterfs/4.0.1/xlator/features/quota.so
/usr/lib64/glusterfs/4.0.1/xlator/features/quotad.so
/usr/lib64/glusterfs/4.0.1/xlator/features/read-only.so
/usr/lib64/glusterfs/4.0.1/xlator/features/sdfs.so
/usr/lib64/glusterfs/4.0.1/xlator/features/selinux.so
/usr/lib64/glusterfs/4.0.1/xlator/features/shard.so
/usr/lib64/glusterfs/4.0.1/xlator/features/snapview-client.so
/usr/lib64/glusterfs/4.0.1/xlator/features/snapview-server.so
/usr/lib64/glusterfs/4.0.1/xlator/features/trash.so
/usr/lib64/glusterfs/4.0.1/xlator/features/upcall.so
/usr/lib64/glusterfs/4.0.1/xlator/features/worm.so
/usr/lib64/glusterfs/4.0.1/xlator/meta.so
/usr/lib64/glusterfs/4.0.1/xlator/mgmt/glusterd.so
/usr/lib64/glusterfs/4.0.1/xlator/mount/api.so
/usr/lib64/glusterfs/4.0.1/xlator/mount/fuse.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/decompounder.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/io-cache.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/io-threads.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/md-cache.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/nl-cache.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/open-behind.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/quick-read.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/read-ahead.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/readdir-ahead.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/stat-prefetch.so
/usr/lib64/glusterfs/4.0.1/xlator/performance/write-behind.so
/usr/lib64/glusterfs/4.0.1/xlator/protocol/client.so
/usr/lib64/glusterfs/4.0.1/xlator/protocol/server.so
/usr/lib64/glusterfs/4.0.1/xlator/storage/posix.so
/usr/lib64/glusterfs/4.0.1/xlator/system/posix-acl.so
/usr/lib64/glusterfs/4.0.1/xlator/testing/features/template.so
/usr/lib64/glusterfs/4.0.1/xlator/testing/performance/symlink-cache.so
/usr/lib64/libgfapi.so.0
/usr/lib64/libgfapi.so.0.0.0
/usr/lib64/libgfchangelog.so.0
/usr/lib64/libgfchangelog.so.0.0.1
/usr/lib64/libgfdb.so.0
/usr/lib64/libgfdb.so.0.0.1
/usr/lib64/libgfrpc.so.0
/usr/lib64/libgfrpc.so.0.0.1
/usr/lib64/libgfxdr.so.0
/usr/lib64/libgfxdr.so.0.0.1
/usr/lib64/libglusterfs.so.0
/usr/lib64/libglusterfs.so.0.0.1

%files python
%defattr(-,root,root,-)
