# Generated by go2rpm

# Fails randomly

%bcond_with check



# https://github.com/spacemonkeygo/openssl

%global goipath         github.com/spacemonkeygo/openssl


Version:        0
%gometa


%global godevelheader %{expand:

Requires:       openssl-devel}



%global common_description %{expand:

Package Openssl is a light wrapper around OpenSSL for Go.



It strives to provide a near-drop-in replacement for the Go standard library tls

package.}



%global golicenses      LICENSE

%global godocs          AUTHORS README.md



Name:           %{goname}



Release:        0.20220602083921924174.master%{?dist}

Summary:        OpenSSL bindings for Go



# Upstream license specification: Apache-2.0

License:        ASL 2.0

URL:            %{gourl}

Source0:        openssl-0.tar.gz



BuildRequires:  golang(github.com/spacemonkeygo/spacelog)

BuildRequires:  openssl-devel



%description

%{common_description}



%gopkg


%prep

%goprep


%install

%gopkginstall


%if %{with check}

%check

%gocheck

%endif



%gopkgfiles


%changelog
* Thu Jun 02 2022 Laura Barcziova <lbarczio@redhat.com> - 0-0.20220602083921924174.master
- Development snapshot (c2dcc5cc)


* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12

- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild



* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11

- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild



* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10

- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild



* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9

- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild



* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8

- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild



* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7

- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild



* Wed May 29 16:42:06 CEST 2019 Robert-Andr√© Mauchin <zebob.m@gmail.com> - 0-0.6.20190529gitc2dcc5c

- Bump to commit c2dcc5cca94ac8f7f3f0c20e20050d4cce9d9730



* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20171219gite863d83

- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild



* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171219gite863d83

- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild



* Mon Feb 12 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 0-0.3.20171219gite863d83

- Remove extra buildmode flag, that's already in gotest



* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171219gite863d83

- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild



* Mon Jan 15 2018 Marek Skalick√Ĺ <mskalick@redhat.com> - 0-0.1.20171219gite863d83

- First package for Fedora
