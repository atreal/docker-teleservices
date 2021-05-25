branch=use-modules-from-git-clones

pull:
		docker-compose pull

clean:
		docker-compose kill
		docker-compose rm
		sudo rm -fr data/*/*/ data/wcs/config.pck data/wcs/.rnd

run:
		docker-compose -f docker-compose-$(branch).yml up

build:
		docker-compose -f docker-compose-$(branch).yml build
build-no-cache:
		docker-compose -f docker-compose-$(branch).yml build --no-cache

run-buster:
		make run branch=buster
build-buster:
		make build branch=buster
build-no-cache-buster:
		make build-no-cache branch=buster

run-buster-test:
		make run branch=buster-test
build-buster-test:
		make build branch=buster-test
build-no-cache-buster-test:
		make build-no-cache branch=buster-test
