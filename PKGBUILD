pkgname=hw-zsh-config-git
pkgver=0.1.0
pkgrel=1
pkgdesc="Hendrik's grml zsh setup."
arch=('any')
url="http://gitlab.com/w0lff/hw-zsh-config"
license=('GPL')
depends=('coreutils' 'grep' 'inetutils' 'procps' 'sed' 'zsh')
makedepends=('git')
conflicts=('grml-zsh-config')
provides=('grml-zsh-config' 'grmlzshrc')
source=("$pkgname"::'git+https://gitlab.com/w0lff/hw-zsh-config.git')
sha1sums=('SKIP')

pkgver(){
  cd "$srcdir/$pkgname"
  git describe --long | sed -E 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  true
}

package() {
  cd "$srcdir/$pkgname"
  install -Dm644 zshrc-home.zsh "$pkgdir/etc/skel/.zshrc"
  install -Dm644 zshrc-base-hw.zsh "$pkgdir/etc/zsh/zshrc"
}

# vim:set ts=2 sw=2 et:
