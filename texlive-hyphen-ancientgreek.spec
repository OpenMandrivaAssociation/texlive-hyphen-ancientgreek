%global tl_name hyphen-ancientgreek
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ancient Greek hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-ancientgreek
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-ancientgreek.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Ancient Greek in LGR and UTF-8 encodings,
including support for (obsolete) Ibycus font encoding. Patterns in UTF-8
use two code positions for each of the vowels with acute accent (a.k.a
tonos, oxia), e.g., U+03AE, U+1F75 for eta.

