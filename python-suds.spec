Summary: Lightweight SOAP client
Name:    python-suds
Version: 0.4.1
Release: 1
Source0: https://fedorahosted.org/releases/s/u/suds/%{name}-%{version}.tar.gz
License: GPL3
Group: Development/Python
Prefix: %{_prefix}
BuildArch: noarch
Url: https://fedorahosted.org/suds
AutoReq: 0

BuildRequires: python-devel python-setuptools

%description
suds

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install  --root=%{buildroot} --record=INSTALLED_FILES

touch DIRS
for i in `cat INSTALLED_FILES`; do
    if [ -f %{buildroot}/$i ]; then
	echo $i >>FILES
    fi
    if [ -d %{buildroot}/$i ]; then
	echo %dir $i >>DIRS
    fi
done

sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

%clean

%files -f INSTALLED_FILES
