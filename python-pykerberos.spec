#
# Conditional build:
%bcond_with	krb5	# MIT Kerberos instead of heimdal
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	High-level interface to Kerberos
Summary(pl.UTF-8):	Wysokopoziomowy interfejs do Kerberosa
Name:		python-pykerberos
Version:	1.2.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pykerberos/
Source0:	https://files.pythonhosted.org/packages/source/p/pykerberos/pykerberos-%{version}.tar.gz
# Source0-md5:	3a1095035ef26f9551cdfc2a52ee02a5
Patch0:		pykerberos-heimdal.patch
URL:		https://pypi.org/project/pykerberos/
%if %{with krb5}
BuildRequires:	krb5-devel
%else
BuildRequires:	heimdal-devel
%endif
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI)
operations. The goal is to avoid having to build a module that wraps
the entire Kerberos framework, and instead offer a limited set of
functions that do what is needed for client/server Kerberos
authentication based on <http://www.ietf.org/rfc/rfc4559.txt>.

%description -l pl.UTF-8
Ten moduł Pythona to wysokopoziomowe obudowanie operacji Kerberosa
(GSSAPI). Celem jest uniknięcie potrzeby budowania moduł opakowującego
cały szkielet Kerberosa na rzecz ograniczonego zbioru funkcji,
wystarczających do uwierzytelniania klienta/serwera Kerberosa w
oparciu o <http://www.ietf.org/rfc/rfc4559.txt>.

%package -n python3-pykerberos
Summary:	High-level interface to Kerberos
Summary(pl.UTF-8):	Wysokopoziomowy interfejs do Kerberosa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pykerberos
This Python package is a high-level wrapper for Kerberos (GSSAPI)
operations. The goal is to avoid having to build a module that wraps
the entire Kerberos framework, and instead offer a limited set of
functions that do what is needed for client/server Kerberos
authentication based on <http://www.ietf.org/rfc/rfc4559.txt>.

%description -n python3-pykerberos -l pl.UTF-8
Ten moduł Pythona to wysokopoziomowe obudowanie operacji Kerberosa
(GSSAPI). Celem jest uniknięcie potrzeby budowania moduł opakowującego
cały szkielet Kerberosa na rzecz ograniczonego zbioru funkcji,
wystarczających do uwierzytelniania klienta/serwera Kerberosa w
oparciu o <http://www.ietf.org/rfc/rfc4559.txt>.

%prep
%setup -q -n pykerberos-%{version}
%patch -P0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt pysrc/kerberos.py
%{py_sitedir}/kerberos.so
%{py_sitedir}/pykerberos-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pykerberos
%defattr(644,root,root,755)
%doc README.txt pysrc/kerberos.py
%{py3_sitedir}/kerberos.cpython-*.so
%{py3_sitedir}/pykerberos-%{version}-py*.egg-info
%endif
