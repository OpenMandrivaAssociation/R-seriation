%global packname  seriation
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.10
Release:          1
Summary:          Infrastructure for seriation
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/seriation_1.0-10.tar.gz
Requires:         R-stats R-cluster R-TSP R-gclus R-grid R-colorspace 
Requires:         R-MASS R-biclust
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-cluster R-TSP R-gclus R-grid R-colorspace
BuildRequires:    R-MASS R-biclust

%description
Infrastructure for seriation with an implementation of several
seriation/sequencing techniques to reorder matrices, dissimilarity
matrices, and dendrograms. Also contains some visualizations techniques
based on seriation.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

