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
