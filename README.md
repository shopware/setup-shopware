# Setup Shopware

Setup Shopware in your GitHub Actions pipeline to run tests.

## Usage

```yaml
- name: Setup Shopware
  uses: FriendsOfShopware/setup-shopware@v1
  with:
    shopware-version: v6.5.3.2
    php-version: 8.1
```

The `php-version` can be any PHP version supported by [setup-php](https://github.com/shivammathur/setup-php). 

## Example pipeline to run PHPUnit tests

```yaml
jobs:
    phpunit:
        runs-on: ubuntu-latest
        steps:
            - name: Setup Shopware
              uses: FriendsOfShopware/setup-shopware@main
              with:
                shopware-version: '6.5.7.3'
                php-version: 8.1

            - name: Checkout
              uses: actions/checkout@v3
              with:
                  path: custom/plugins/FroshPlatformTemplateMail

            - name: Run Tests
              run: |
                  cd custom/plugins/FroshPlatformTemplateMail/
                  php -d pcov.enabled=1 ../../../vendor/bin/phpunit --coverage-clover clover.xml

```
