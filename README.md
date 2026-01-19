# Setup Shopware

This GitHub action helps you set up Shopware, PHP, MySQL, Node.js, and other requirements in your GitHub Actions workflows for unit testing, end-to-end testing, and custom CI/CD workflows.

## Features

- **Easy setup**: Install Shopware from any repository and version.
- **PHP & Composer**: Set up PHP (with optional extensions) and Composer.
- **Database**: Automatically configures MySQL.
- **Custom install**: Optionally install Shopware with locale and currency.
- **Asset building**: Optionally build Administration and Storefront assets.
- **Test-ready**: Supports PHPUnit and E2E test environments.


## Inputs

| Name                   | Description                                                        | Default         | Required |
|------------------------|--------------------------------------------------------------------|-----------------|----------|
| `env`                  | Environment type: `test` for PHPUnit, `e2e` for end-to-end.        | `test`          | false    |
| `shopware-version`     | Shopware version to install (e.g. `v6.5.3.2`).                     |                 | true     |
| `shopware-repository`  | GitHub repository to clone Shopware from.                          | `shopware/shopware` | true |
| `php-version`          | PHP version (compatible with [shivammathur/setup-php]).            | `8.2`           | false    |
| `php-extensions`       | Comma-separated list of PHP extensions.                            |                 | false    |
| `php-ini-values`       | PHP ini values to set (e.g. `post_max_size=256M`).                 | `session.gc_probability=0` | false    |
| `composer-root-version`| Set the COMPOSER_ROOT_VERSION. `.auto` to discover from composer.json | `.auto`       | false    |
| `install`              | Whether to run the Shopware installer.                             | `false`         | true     |
| `install-locale`       | Locale for Shopware installation.                                  | `en-GB`         | true     |
| `install-currency`     | Currency for Shopware installation.                                | `EUR`           | true     |
| `install-admin`        | Build the Administration.                                          |                 | false    |
| `install-storefront`   | Build the Storefront.                                              |                 | false    |
| `keep-composer-tools`  | Keep Composer tools (PHPStan, ECS, BC-Checker) after install.      | `false`         | true     |
| `mysql-version`        | MySQL image to use, or `builtin` for GitHub-hosted MySQL.          | `builtin`       | false    |
| `node-version`         | Node.js version (e.g. `20.x`).                                    | `20.x`          | false    |
| `path`                 | Directory in `$GITHUB_WORKSPACE` to clone Shopware into.           |                 | true     |

## Example pipeline to run PHPUnit tests

```yaml
jobs:
    phpunit:
        runs-on: ubuntu-latest
        steps:
            - name: Setup Shopware
              uses: shopware/setup-shopware@v1
              with:
                env: test
                shopware-version: v6.5.3.2
                shopware-repository: shopware/shopware
                php-version: 8.1
                install: true

