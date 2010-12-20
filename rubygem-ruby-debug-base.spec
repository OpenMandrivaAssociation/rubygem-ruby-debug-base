%define oname ruby-debug-base

Name:       rubygem-%{oname}
Version:    0.10.3
Release:    %mkrel 1
Summary:    Fast Ruby debugger - core component
Group:      Development/Ruby
License:    MIT
URL:        http://rubyforge.org/projects/ruby-debug/
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(linecache) >= 0.3
BuildRequires: rubygems
Provides:   rubygem(%{oname}) = %{version}

%description
ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component 
provides support that front-ends can build on. It provides breakpoint 
handling, bindings for stack frames among other things.


%prep
%setup -q
tar xmf data.tar.gz

%build
%gem_build

%install
rm -rf %{buildroot}
%gem_install

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/ruby_debug.so
