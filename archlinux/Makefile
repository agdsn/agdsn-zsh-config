build:
	makepkg -sirc -p PKGBUILD

local: dev.PKGBUILD
	makepkg -sirc -p dev.PKGBUILD

dev.PKGBUILD: PKGBUILD
	sed -e "s#git+https://.*#git+file://$(PWD)')#" PKGBUILD > dev.PKGBUILD

clean: 
	rm dev.PKGBUILD
	rm hw-zsh-config-git-*.pkg.tar.zst
	rm hw-zsh-config-git -rf

