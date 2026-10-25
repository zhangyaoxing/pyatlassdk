"""Generated resource for Rules. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.default_rule import DefaultRule
from pyatlassdk.app.models.default_rule_constructor import DefaultRuleConstructor
from pyatlassdk.app.models.rule import Rule
from pyatlassdk.app.models.third_party_service_rule import ThirdPartyServiceRule

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Rules:
    """View and manage your application's [data access rules](https://www.mongodb.com/docs/atlas/app-services/rules/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_delete_default_rule(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> None:
        """
        Delete default roles and filters

        Delete the [default roles and filters](https://www.mongodb.com/docs/atlas/app-services/rules/#default-rules) of a data source.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/default_rule"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_default_rule(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> DefaultRule:
        """
        Get default roles and filters

        Get the current [default roles and filters](https://www.mongodb.com/docs/atlas/app-services/rules/#default-rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/default_rule"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DefaultRule,
        )

    def admin_create_default_rule(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        body: DefaultRuleConstructor,
    ) -> DefaultRule:
        """
        Create default roles and filters

        Create [default roles and filters](https://www.mongodb.com/docs/atlas/app-services/rules/#default-rules) for a data source.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body: A default rule configuration object.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/default_rule"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=DefaultRule,
            content_type="application/json",
        )

    def admin_update_default_rule(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        body: dict[str, Any],
    ) -> None:
        """
        Update default roles and filters

        Modify the [default roles and filters](https://www.mongodb.com/docs/atlas/app-services/rules/#default-rules) of a data source.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body: The updated default rule configuration object.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/default_rule"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_list_rules(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> Any:
        """
        Get all rules

        List all [data access rules](https://www.mongodb.com/docs/atlas/app-services/rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/rules"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_rule(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        body: Rule | ThirdPartyServiceRule,
    ) -> dict[str, Any]:
        """
        Create a rule

        Create a [data access rule](https://www.mongodb.com/docs/atlas/app-services/rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body: The rule to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/rules"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_rule(
        self,
        app_id: str,
        group_id: str,
        rule_id: str,
        service_id: str,
    ) -> None:
        """
        Delete a rule

        Delete a [data access rule](https://www.mongodb.com/docs/atlas/app-services/rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            rule_id: The unique `_id` value of a rule.
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/rules/{quote(str(rule_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_rule(
        self,
        app_id: str,
        group_id: str,
        rule_id: str,
        service_id: str,
    ) -> Rule | ThirdPartyServiceRule:
        """
        Get a rule

        Get a specific [data access rule](https://www.mongodb.com/docs/atlas/app-services/rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            rule_id: The unique `_id` value of a rule.
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/rules/{quote(str(rule_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Rule | ThirdPartyServiceRule,
        )

    def admin_update_rule(
        self,
        app_id: str,
        group_id: str,
        rule_id: str,
        service_id: str,
        body: Rule | ThirdPartyServiceRule,
    ) -> None:
        """
        Update a rule

        Update a [data access rule](https://www.mongodb.com/docs/atlas/app-services/rules).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            rule_id: The unique `_id` value of a rule.
            service_id: The unique `_id` value of a service.
            body: The new state of the rule.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/rules/{quote(str(rule_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
