# Generated from ruby-debug-base-0.10.3.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	ruby-debug-base

Summary:	Fast Ruby debugger - core component
Name:		rubygem-%{rbname}

Version:	0.10.3
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://rubyforge.org/projects/ruby-debug/
Source0:	%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel

%description
ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component 
provides support that front-ends can build on. It provides breakpoint 
handling, bindings for stack frames among other things.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%check
rake test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/ChangeLog
%{ruby_sitearchdir}.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
