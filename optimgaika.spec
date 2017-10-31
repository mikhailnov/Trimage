Summary:	Tool for Optimizing PNG and JPEG Files
Name:		optimgaika
Version:	1.2.1
Release:	1
License:	MIT
Group:		Graphics
Url:		https://github.com/mikhailnov/optimgaika
Source0:	https://github.com/mikhailnov/optimgaika/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	advancecomp
Requires:	guetzli
Requires:	optipng
Requires:	pngcrush
Requires:	PyQt4
BuildArch:	noarch

%description
optimgaika is a cross-platform GUI and command-line interface to optimize
image files via optipng, pngcrush, advpng and guetzli, depending on
the filetype (currently, PNG and JPEG files are supported). It was
inspired by imageoptim. All image files are losslessy compressed on
the highest available compression levels. optimgaika gives you various
input functions to fit your own workflow: a regular file dialog,
dragging and dropping and various command line options.

%files
%doc COPYING README resources/todo
%{_bindir}/%{name}
%{python_sitelib}/%{name}/*
%{python_sitelib}/%{name}-*
%{_mandir}/man1/*
%{_datadir}/applications/optimgaika.desktop
%{_datadir}/icons/hicolor/scalable/apps/optimgaika.svg

#------------------------------------------------------------------

%prep
%setup -q

%build

%install
PYTHONDONTWRITEBYTECODE=1 python setup.py install --root=%{buildroot}

%changelog

* Tue Oct 31 2017 Rosa <rosa@abf.rosalinux.ru> 1.2.1-1
- (e7b6e53) Automatic import for version 1.2.1-1


