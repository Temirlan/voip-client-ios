# -*- rpm-spec -*-
# 
# msamr - AMR codec plugin for mediastreamer2
# 

Summary:	AMR codec plugin for mediastreamer2
Name:		msamr
Version:	0.0.1
Release:	1
License:	GPL
Group:		Applications/Communications
URL:		http://www.belledonne-communications.com
Source0:	%{name}-0.0.1.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%ifarch %ix86
BuildArch:	i686
%endif
Requires: bash >= 2.0

%description
AMR codec plugin for mediastreamer2, based on opencore-amr

%prep
%setup -q

%build
%configure 
%{__make} 

# parallel build disabled due to automake libtool random errors
#%{__make} -j$RPM_BUILD_NCPUS 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*


%changelog
* Tue Oct 19 2010 Simon Morlat <simon.morlat@belledonne-communications.com>
	- Initial specfile.

