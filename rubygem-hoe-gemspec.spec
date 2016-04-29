#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe-gemspec
Version  : 1.0.0
Release  : 5
URL      : https://rubygems.org/downloads/hoe-gemspec-1.0.0.gem
Source0  : https://rubygems.org/downloads/hoe-gemspec-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rubyforge
BuildRequires : rubygem-test-unit
Patch1: 0001-Fix-hoe-version-conflict.patch

%description
= hoe-gemspec
* http://github.com/flavorjones/hoe-gemspec
== DESCRIPTION:
Generate a prerelease gemspec based on a Hoe spec.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-gemspec-1.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-hoe-gemspec.gemspec
%patch1 -p1

%build
gem build rubygem-hoe-gemspec.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-gemspec-1.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/hoe-gemspec-1.0.0
ruby -v -I.:lib:test test*/test_*.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/hoe-gemspec-1.0.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/Hoe/Gemspec/cdesc-Gemspec.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/Hoe/Gemspec/define_gemspec_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/Hoe/cdesc-Hoe.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/page-CHANGELOG_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-gemspec-1.0.0/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/lib/hoe/gemspec.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/README.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/fixture_project.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/lib/fixture_project.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/fixture_project/test/test_fixture_project.rb
/usr/lib64/ruby/gems/2.2.0/gems/hoe-gemspec-1.0.0/test/test_hoe_gemspec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/hoe-gemspec-1.0.0.gemspec
