Name:		cloud-utils-growpart
Version:	0.27
Release:	11%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	https://launchpad.net/cloud-utils/trunk/%{version}/+download/cloud-utils-%{version}.tar.gz
Source1:	LICENSE
Patch0:		0001-supress-partx-usage-error.patch

BuildArch:	noarch

Summary:	Script for growing a partition
Group:		System Environment/Base

Requires:	gawk
Requires:	util-linux
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk

%description
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%prep
%setup -q -n cloud-utils-%{version}
%patch0 -p1

%build

%install
cp %{SOURCE1} LICENSE

# Create the target directories
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

# Install the growpart binary and man page
cp bin/growpart $RPM_BUILD_ROOT/%{_bindir}/
cp man/growpart.* $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%doc ChangeLog LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*

%changelog
* Tue Jan 14 2014 Lars Kellogg-Stedman <lars@redhat.com> - 0.27-11
- import into RHEL

