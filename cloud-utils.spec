Summary:	Cloud image management utilities
Name:		cloud-utils
Version:	0.27
Release:	3%{?dist}
License:	GPLv3
Group:		System Environment/Base
URL:		https://launchpad.net/cloud-utils/trunk/0.27/+download/cloud-utils-0.27.tar.gz

Source0:	%{name}-%{version}.tar.gz
Source1:        LICENSE

BuildArch:	noarch

%if 0%{?rhel}
# Exclude EPEL architectures that don't have qemu-img
ExcludeArch:	i386 ppc64
%endif

Requires:	gawk
Requires:	gdisk
Requires:	e2fsprogs
Requires:	euca2ools
Requires:	file
Requires:	python
Requires:	python-paramiko
Requires:	qemu-img
Requires:	util-linux

%description
This package provides a useful set of utilities for managing cloud images.

The euca2ools package (a dependency of cloud-utils) provides an Amazon EC2 API
compatible set of utilities for bundling kernels, ramdisks, and root
filesystems, and uploading them to either EC2 or UEC.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.


%prep
%setup -q


%build


%install
cp %{SOURCE1} LICENSE

# Install binaries
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp bin/* $RPM_BUILD_ROOT/%{_bindir}/
# Exclude Ubuntu-specific tools
rm $RPM_BUILD_ROOT/%{_bindir}/*ubuntu*

# Install man pages
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp man/* $RPM_BUILD_ROOT/%{_mandir}/man1/


%files
%doc ChangeLog LICENSE
%{_bindir}/*
%doc %{_mandir}/man1/*


%changelog
* Mon Apr  8 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-3
- 3rd attempt to fix the spec file to only build on x86_64 for EPEL.

* Tue Apr  5 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-2
- Yet another spec file fix to only build on x86_64 for EPEL.

* Tue Apr  2 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-1
- Update to upstream release 0.27.
- Fix spec file to only build on x86_64 for EPEL.

* Wed Feb 12 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-0.2.bzr216
- Add GPL-3 license.
- Exclude Ubuntu-specific tools.
- Fix some spec file issues per reviewers comments.

* Tue Feb  5 2013 Juerg Haefliger <juergh@gmail.com> - 0.27-0.1.bzr216
- Initial build based on upstream revision bzr216.
