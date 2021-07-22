#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glusterfs
Version  : 7.5
Release  : 39
URL      : https://download.gluster.org/pub/gluster/glusterfs/7/7.5/glusterfs-7.5.tar.gz
Source0  : https://download.gluster.org/pub/gluster/glusterfs/7/7.5/glusterfs-7.5.tar.gz
Summary  : Distributed File System
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: glusterfs-bin = %{version}-%{release}
Requires: glusterfs-data = %{version}-%{release}
Requires: glusterfs-lib = %{version}-%{release}
Requires: glusterfs-libexec = %{version}-%{release}
Requires: glusterfs-license = %{version}-%{release}
Requires: glusterfs-man = %{version}-%{release}
Requires: glusterfs-python = %{version}-%{release}
Requires: glusterfs-python3 = %{version}-%{release}
Requires: glusterfs-services = %{version}-%{release}
Requires: rpcbind
BuildRequires : acl-dev
BuildRequires : bison
BuildRequires : curl-dev
BuildRequires : flex
BuildRequires : fuse-dev
BuildRequires : intltool-dev
BuildRequires : libaio-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(liburcu-bp)
BuildRequires : pkgconfig(liburcu-cds)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3-dev
BuildRequires : rdma-core-dev
BuildRequires : readline-dev
BuildRequires : rpcbind
BuildRequires : xz-dev

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
Requires: glusterfs-data = %{version}-%{release}
Requires: glusterfs-libexec = %{version}-%{release}
Requires: glusterfs-license = %{version}-%{release}
Requires: glusterfs-services = %{version}-%{release}

%description bin
bin components for the glusterfs package.


%package data
Summary: data components for the glusterfs package.
Group: Data

%description data
data components for the glusterfs package.


%package dev
Summary: dev components for the glusterfs package.
Group: Development
Requires: glusterfs-lib = %{version}-%{release}
Requires: glusterfs-bin = %{version}-%{release}
Requires: glusterfs-data = %{version}-%{release}
Provides: glusterfs-devel = %{version}-%{release}
Requires: glusterfs = %{version}-%{release}

%description dev
dev components for the glusterfs package.


%package doc
Summary: doc components for the glusterfs package.
Group: Documentation
Requires: glusterfs-man = %{version}-%{release}

%description doc
doc components for the glusterfs package.


%package lib
Summary: lib components for the glusterfs package.
Group: Libraries
Requires: glusterfs-data = %{version}-%{release}
Requires: glusterfs-libexec = %{version}-%{release}
Requires: glusterfs-license = %{version}-%{release}

%description lib
lib components for the glusterfs package.


%package libexec
Summary: libexec components for the glusterfs package.
Group: Default
Requires: glusterfs-license = %{version}-%{release}

%description libexec
libexec components for the glusterfs package.


%package license
Summary: license components for the glusterfs package.
Group: Default

%description license
license components for the glusterfs package.


%package man
Summary: man components for the glusterfs package.
Group: Default

%description man
man components for the glusterfs package.


%package python
Summary: python components for the glusterfs package.
Group: Default
Requires: glusterfs-python3 = %{version}-%{release}

%description python
python components for the glusterfs package.


%package python3
Summary: python3 components for the glusterfs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the glusterfs package.


%package services
Summary: services components for the glusterfs package.
Group: Systemd services

%description services
services components for the glusterfs package.


%prep
%setup -q -n glusterfs-7.5
cd %{_builddir}/glusterfs-7.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587872455
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%reconfigure --disable-static --localstatedir=/usr/share/glusterfs PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1587872455
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glusterfs
cp %{_builddir}/glusterfs-7.5/COPYING-GPLV2 %{buildroot}/usr/share/package-licenses/glusterfs/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/glusterfs-7.5/COPYING-LGPLV3 %{buildroot}/usr/share/package-licenses/glusterfs/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/glusterfs-7.5/contrib/fuse-util/COPYING %{buildroot}/usr/share/package-licenses/glusterfs/dfac199a7539a404407098a2541b9482279f690d
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/ocf/resource.d/glusterfs/glusterd
/usr/lib/ocf/resource.d/glusterfs/volume

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

%files data
%defattr(-,root,root,-)
/usr/share/glusterfs/lib/glusterd/groups/db-workload
/usr/share/glusterfs/lib/glusterd/groups/distributed-virt
/usr/share/glusterfs/lib/glusterd/groups/gluster-block
/usr/share/glusterfs/lib/glusterd/groups/metadata-cache
/usr/share/glusterfs/lib/glusterd/groups/nl-cache
/usr/share/glusterfs/lib/glusterd/groups/samba
/usr/share/glusterfs/lib/glusterd/groups/virt
/usr/share/glusterfs/lib/glusterd/hooks/1/add-brick/post/S10selinux-label-brick.sh
/usr/share/glusterfs/lib/glusterd/hooks/1/add-brick/post/S13create-subdir-mounts.sh
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
/usr/share/glusterfs/scripts/setup-thin-arbiter.sh
/usr/share/glusterfs/scripts/slave-upgrade.sh
/usr/share/glusterfs/scripts/stop-all-gluster-processes.sh

%files dev
%defattr(-,root,root,-)
/usr/include/glusterfs/api/glfs-handles.h
/usr/include/glusterfs/api/glfs.h
/usr/include/glusterfs/async.h
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
/usr/include/glusterfs/daemon.h
/usr/include/glusterfs/default-args.h
/usr/include/glusterfs/defaults.h
/usr/include/glusterfs/dict.h
/usr/include/glusterfs/event-history.h
/usr/include/glusterfs/events.h
/usr/include/glusterfs/fd-lk.h
/usr/include/glusterfs/fd.h
/usr/include/glusterfs/gf-dirent.h
/usr/include/glusterfs/gf-event.h
/usr/include/glusterfs/gfchangelog/changelog.h
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
/usr/lib64/libgfrpc.so
/usr/lib64/libgfxdr.so
/usr/lib64/libglusterfs.so
/usr/lib64/pkgconfig/glusterfs-api.pc
/usr/lib64/pkgconfig/libgfchangelog.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/glusterfs/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/glusterfs/7.5/auth/addr.so
/usr/lib64/glusterfs/7.5/auth/login.so
/usr/lib64/glusterfs/7.5/cloudsync-plugins/cloudsynccvlt.so
/usr/lib64/glusterfs/7.5/cloudsync-plugins/cloudsyncs3.so
/usr/lib64/glusterfs/7.5/rpc-transport/rdma.so
/usr/lib64/glusterfs/7.5/rpc-transport/socket.so
/usr/lib64/glusterfs/7.5/xlator/cluster/afr.so
/usr/lib64/glusterfs/7.5/xlator/cluster/dht.so
/usr/lib64/glusterfs/7.5/xlator/cluster/disperse.so
/usr/lib64/glusterfs/7.5/xlator/cluster/distribute.so
/usr/lib64/glusterfs/7.5/xlator/cluster/ec.so
/usr/lib64/glusterfs/7.5/xlator/cluster/nufa.so
/usr/lib64/glusterfs/7.5/xlator/cluster/replicate.so
/usr/lib64/glusterfs/7.5/xlator/cluster/switch.so
/usr/lib64/glusterfs/7.5/xlator/debug/delay-gen.so
/usr/lib64/glusterfs/7.5/xlator/debug/error-gen.so
/usr/lib64/glusterfs/7.5/xlator/debug/io-stats.so
/usr/lib64/glusterfs/7.5/xlator/debug/sink.so
/usr/lib64/glusterfs/7.5/xlator/debug/trace.so
/usr/lib64/glusterfs/7.5/xlator/features/access-control.so
/usr/lib64/glusterfs/7.5/xlator/features/arbiter.so
/usr/lib64/glusterfs/7.5/xlator/features/barrier.so
/usr/lib64/glusterfs/7.5/xlator/features/bit-rot.so
/usr/lib64/glusterfs/7.5/xlator/features/bitrot-stub.so
/usr/lib64/glusterfs/7.5/xlator/features/cdc.so
/usr/lib64/glusterfs/7.5/xlator/features/changelog.so
/usr/lib64/glusterfs/7.5/xlator/features/cloudsync.so
/usr/lib64/glusterfs/7.5/xlator/features/gfid-access.so
/usr/lib64/glusterfs/7.5/xlator/features/index.so
/usr/lib64/glusterfs/7.5/xlator/features/leases.so
/usr/lib64/glusterfs/7.5/xlator/features/locks.so
/usr/lib64/glusterfs/7.5/xlator/features/marker.so
/usr/lib64/glusterfs/7.5/xlator/features/namespace.so
/usr/lib64/glusterfs/7.5/xlator/features/posix-locks.so
/usr/lib64/glusterfs/7.5/xlator/features/quiesce.so
/usr/lib64/glusterfs/7.5/xlator/features/quota.so
/usr/lib64/glusterfs/7.5/xlator/features/quotad.so
/usr/lib64/glusterfs/7.5/xlator/features/read-only.so
/usr/lib64/glusterfs/7.5/xlator/features/sdfs.so
/usr/lib64/glusterfs/7.5/xlator/features/selinux.so
/usr/lib64/glusterfs/7.5/xlator/features/shard.so
/usr/lib64/glusterfs/7.5/xlator/features/snapview-client.so
/usr/lib64/glusterfs/7.5/xlator/features/snapview-server.so
/usr/lib64/glusterfs/7.5/xlator/features/thin-arbiter.so
/usr/lib64/glusterfs/7.5/xlator/features/trash.so
/usr/lib64/glusterfs/7.5/xlator/features/upcall.so
/usr/lib64/glusterfs/7.5/xlator/features/utime.so
/usr/lib64/glusterfs/7.5/xlator/features/worm.so
/usr/lib64/glusterfs/7.5/xlator/meta.so
/usr/lib64/glusterfs/7.5/xlator/mgmt/glusterd.so
/usr/lib64/glusterfs/7.5/xlator/mount/api.so
/usr/lib64/glusterfs/7.5/xlator/mount/fuse.so
/usr/lib64/glusterfs/7.5/xlator/performance/io-cache.so
/usr/lib64/glusterfs/7.5/xlator/performance/io-threads.so
/usr/lib64/glusterfs/7.5/xlator/performance/md-cache.so
/usr/lib64/glusterfs/7.5/xlator/performance/nl-cache.so
/usr/lib64/glusterfs/7.5/xlator/performance/open-behind.so
/usr/lib64/glusterfs/7.5/xlator/performance/quick-read.so
/usr/lib64/glusterfs/7.5/xlator/performance/read-ahead.so
/usr/lib64/glusterfs/7.5/xlator/performance/readdir-ahead.so
/usr/lib64/glusterfs/7.5/xlator/performance/stat-prefetch.so
/usr/lib64/glusterfs/7.5/xlator/performance/write-behind.so
/usr/lib64/glusterfs/7.5/xlator/playground/template.so
/usr/lib64/glusterfs/7.5/xlator/protocol/client.so
/usr/lib64/glusterfs/7.5/xlator/protocol/server.so
/usr/lib64/glusterfs/7.5/xlator/storage/posix.so
/usr/lib64/glusterfs/7.5/xlator/system/posix-acl.so
/usr/lib64/libgfapi.so.0
/usr/lib64/libgfapi.so.0.0.0
/usr/lib64/libgfchangelog.so.0
/usr/lib64/libgfchangelog.so.0.0.1
/usr/lib64/libgfrpc.so.0
/usr/lib64/libgfrpc.so.0.0.1
/usr/lib64/libgfxdr.so.0
/usr/lib64/libgfxdr.so.0.0.1
/usr/lib64/libglusterfs.so.0
/usr/lib64/libglusterfs.so.0.0.1

%files libexec
%defattr(-,root,root,-)
/usr/libexec/glusterfs/gfevents/__init__.py
/usr/libexec/glusterfs/gfevents/eventsapiconf.py
/usr/libexec/glusterfs/gfevents/eventtypes.py
/usr/libexec/glusterfs/gfevents/gf_event.py
/usr/libexec/glusterfs/gfevents/glustereventsd.py
/usr/libexec/glusterfs/gfevents/handlers.py
/usr/libexec/glusterfs/gfevents/utils.py
/usr/libexec/glusterfs/gfind_missing_files/gcrawler
/usr/libexec/glusterfs/gfind_missing_files/gfid_to_path.py
/usr/libexec/glusterfs/gfind_missing_files/gfid_to_path.sh
/usr/libexec/glusterfs/gfind_missing_files/gfind_missing_files.sh
/usr/libexec/glusterfs/glusterfind/S57glusterfind-delete-post.py
/usr/libexec/glusterfs/glusterfind/__init__.py
/usr/libexec/glusterfs/glusterfind/brickfind.py
/usr/libexec/glusterfs/glusterfind/changelog.py
/usr/libexec/glusterfs/glusterfind/changelogdata.py
/usr/libexec/glusterfs/glusterfind/conf.py
/usr/libexec/glusterfs/glusterfind/gfind_py2py3.py
/usr/libexec/glusterfs/glusterfind/libgfchangelog.py
/usr/libexec/glusterfs/glusterfind/main.py
/usr/libexec/glusterfs/glusterfind/nodeagent.py
/usr/libexec/glusterfs/glusterfind/tool.conf
/usr/libexec/glusterfs/glusterfind/utils.py
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
/usr/libexec/glusterfs/python/syncdaemon/argsupgrade.py
/usr/libexec/glusterfs/python/syncdaemon/changelogagent.py
/usr/libexec/glusterfs/python/syncdaemon/conf.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncd.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncdconfig.py
/usr/libexec/glusterfs/python/syncdaemon/gsyncdstatus.py
/usr/libexec/glusterfs/python/syncdaemon/libcxattr.py
/usr/libexec/glusterfs/python/syncdaemon/libgfchangelog.py
/usr/libexec/glusterfs/python/syncdaemon/logutils.py
/usr/libexec/glusterfs/python/syncdaemon/master.py
/usr/libexec/glusterfs/python/syncdaemon/monitor.py
/usr/libexec/glusterfs/python/syncdaemon/py2py3.py
/usr/libexec/glusterfs/python/syncdaemon/rconf.py
/usr/libexec/glusterfs/python/syncdaemon/repce.py
/usr/libexec/glusterfs/python/syncdaemon/resource.py
/usr/libexec/glusterfs/python/syncdaemon/subcmds.py
/usr/libexec/glusterfs/python/syncdaemon/syncdutils.py
/usr/libexec/glusterfs/set_geo_rep_pem_keys.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glusterfs/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/glusterfs/dfac199a7539a404407098a2541b9482279f690d
/usr/share/package-licenses/glusterfs/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/gluster-setgfid2path.8
/usr/share/man/man8/gluster.8
/usr/share/man/man8/glusterd.8
/usr/share/man/man8/glusterfs.8
/usr/share/man/man8/glusterfsd.8
/usr/share/man/man8/mount.glusterfs.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/gluster-ta-volume.service
/usr/lib/systemd/system/glusterd.service
/usr/lib/systemd/system/glustereventsd.service
/usr/lib/systemd/system/glusterfssharedstorage.service
