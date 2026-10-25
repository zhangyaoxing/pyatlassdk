"""Generated resource for Invoices. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from datetime import date
from urllib.parse import quote
from pyatlassdk.admin.models.api_public_usage_details_query_request import ApiPublicUsageDetailsQueryRequest
from pyatlassdk.admin.models.billing_invoice import BillingInvoice
from pyatlassdk.admin.models.cost_explorer_filter_request_body import CostExplorerFilterRequestBody
from pyatlassdk.admin.models.cost_explorer_filter_response_view import CostExplorerFilterResponseView
from pyatlassdk.admin.models.cost_explorer_query_result import CostExplorerQueryResult
from pyatlassdk.admin.models.invoice_report_request import InvoiceReportRequest
from pyatlassdk.admin.models.invoice_report_response import InvoiceReportResponse
from pyatlassdk.admin.models.org_associated_invoice_response import OrgAssociatedInvoiceResponse
from pyatlassdk.admin.models.paginated_api_invoice_metadata_view import PaginatedApiInvoiceMetadataView
from pyatlassdk.admin.models.paginated_api_invoice_view import PaginatedApiInvoiceView
from pyatlassdk.admin.models.paginated_api_sku_view import PaginatedApiSKUView
from pyatlassdk.admin.models.paginated_invoice_report_view import PaginatedInvoiceReportView
from pyatlassdk.admin.models.paginated_public_api_usage_details_line_item_view import PaginatedPublicApiUsageDetailsLineItemView
from pyatlassdk.admin.models.sku_response import SkuResponse

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class Invoices:
    """Returns invoices."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def get_org_associated_invoices(
        self,
        org_id: str,
        *,
        include_linked_orgs: bool | None = None,
        month: int | None = None,
        year: int | None = None,
    ) -> OrgAssociatedInvoiceResponse:
        """
        Return Associated Invoices

        Returns a list of invoice IDs for the specified organization and month/year. Optionally includes invoices from linked organizations.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            include_linked_orgs: Whether to include invoices from linked organizations. Defaults to false.
            month: The month for which to retrieve invoices (1-12). Defaults to current month.
            year: The year for which to retrieve invoices. Defaults to current year.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/associatedInvoices"
        params = {
            "includeLinkedOrgs": include_linked_orgs,
            "month": month,
            "year": year,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgAssociatedInvoiceResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_org_billing_cost_explorer_usage_process(
        self,
        org_id: str,
        body: CostExplorerFilterRequestBody,
        *,
        envelope: bool | None = None,
    ) -> CostExplorerFilterResponseView:
        """
        Create One Cost Explorer Query Process

        Creates a query process within the Cost Explorer for the given parameters. A token is returned that can be used to poll the status of the query and eventually retrieve the results.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Filter parameters for the Cost Explorer query.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/billing/costExplorer/usage"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=CostExplorerFilterResponseView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_org_billing_cost_explorer_usage(
        self,
        org_id: str,
        token: str,
        *,
        envelope: bool | None = None,
    ) -> str | CostExplorerQueryResult:
        """
        Return Usage Details for One Cost Explorer Query

        Returns the usage details for a Cost Explorer query, if the query is finished and the data is ready to be viewed. If the data is not ready, a 'processing' response will indicate that another request should be sent later to view the data.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            token: Unique 64 digit string that identifies the Cost Explorer query.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/billing/costExplorer/usage/{quote(str(token), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str | CostExplorerQueryResult,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_org_invoices(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        from_date: date | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        order_by: Literal["desc", "asc"] | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        sort_by: Literal["START_DATE", "END_DATE"] | None = None,
        status_names: list[Literal["PENDING", "CLOSED", "FORGIVEN", "FAILED", "PAID", "FREE", "PREPAID", "INVOICED"]] | None = None,
        to_date: date | None = None,
        view_linked_invoices: bool | None = None,
    ) -> PaginatedApiInvoiceMetadataView:
        """
        Return All Invoices for One Organization

        Returns all invoices that MongoDB issued to the specified organization. This list includes all invoices regardless of invoice status. If you have a cross-organization setup, you can view linked invoices if you have the Organization Billing Admin or Organization Owner role.
        To compute the total owed amount of the invoices - sum up total owed of each invoice. It could be computed as a sum of owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            from_date: Retrieve the invoices the `startDates` of which are greater than or equal to the `fromDate`. If omit, the invoices return will go back to earliest `startDate`.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            order_by: Field used to order the returned invoices by. Use in combination of `sortBy` parameter to control the order of the result.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            sort_by: Field used to sort the returned invoices by. Use in combination with `orderBy` parameter to control the order of the result.
            status_names: Statuses of the invoice to be retrieved. Omit to return invoices of all statuses.
            to_date: Retrieve the invoices the `endDates` of which are smaller than or equal to the `toDate`. If omit, the invoices return will go further to latest `endDate`.
            view_linked_invoices: Flag that indicates whether to return linked invoices in the `linkedInvoices` field.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices"
        params = {
            "envelope": envelope,
            "fromDate": from_date,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "orderBy": order_by,
            "pageNum": page_num,
            "pretty": pretty,
            "sortBy": sort_by,
            "statusNames": status_names,
            "toDate": to_date,
            "viewLinkedInvoices": view_linked_invoices,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiInvoiceMetadataView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_org_invoice_pending(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiInvoiceView:
        """
        Return All Pending Invoices for One Organization

        Returns all invoices accruing charges for the current billing cycle for the specified organization. If you have a cross-organization setup, you can view linked invoices if you have the Organization Billing Admin or Organization Owner Role.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/pending"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiInvoiceView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_org_invoice(
        self,
        invoice_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> str | BillingInvoice:
        """
        Return One Invoice for One Organization

        Returns one invoice that MongoDB issued to the specified organization. A unique 24-hexadecimal digit string identifies the invoice. You can choose to receive this invoice in JSON or CSV format. If you have a cross-organization setup, you can query for a linked invoice if you have the Organization Billing Admin or Organization Owner role.
        To compute the total owed amount of the invoice - sum up total owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.

        Args:
            invoice_id: Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str | BillingInvoice,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_org_invoice_csv(
        self,
        invoice_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> str:
        """
        Return One Invoice as CSV for One Organization

        Returns one invoice that MongoDB issued to the specified organization in CSV format. A unique 24-hexadecimal digit string identifies the invoice. If you have a cross-organization setup, you can query for a linked invoice if you have the Organization Billing Admin or Organization Owner Role.
         To compute the total owed amount of the invoice - sum up total owed amount of each payment included into the invoice. To compute payment's owed amount - use formula `totalBilledCents` * `unitPrice` + `salesTax` - `startingBalanceCents`.

        Args:
            invoice_id: Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}/csv"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str,
            accept="application/vnd.atlas.2023-01-01+csv",
        )

    def search_org_invoice_line_items(
        self,
        invoice_id: str,
        org_id: str,
        body: ApiPublicUsageDetailsQueryRequest,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
    ) -> PaginatedPublicApiUsageDetailsLineItemView:
        """
        Return All Line Items for One Invoice by Invoice ID

        Query the `lineItems` of the specified invoice and return the result JSON. A unique 24-hexadecimal digit string identifies the invoice.

        Args:
            invoice_id: Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            body: Filter parameters for the `lineItems` query. Send a request with an empty JSON body to retrieve all line items for a given `invoiceID` without applying any filters.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}/lineItems:search"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedPublicApiUsageDetailsLineItemView,
            accept="application/vnd.atlas.2024-08-05+json",
            content_type="application/vnd.atlas.2024-08-05+json",
        )

    def list_org_invoice_reports(
        self,
        invoice_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedInvoiceReportView:
        """
        Return All Invoice Reports for One Invoice

        Returns all unexpired reports for the specified invoice, newest first. Listed reports never include a download URL; retrieve a single report to obtain one.

        Args:
            invoice_id: Unique string that identifies the invoice to list reports for.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}/reports"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedInvoiceReportView,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_org_invoice_report(
        self,
        invoice_id: str,
        org_id: str,
        body: InvoiceReportRequest,
    ) -> InvoiceReportResponse:
        """
        Create One Invoice Report

        Requests asynchronous generation of a report for the specified invoice. Returns a report identifier that can be used to poll the report status.

        Args:
            invoice_id: Unique string that identifies the invoice for which to generate the report.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            body: Create Invoice Report request body.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}/reports"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=InvoiceReportResponse,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def get_org_invoice_report(
        self,
        invoice_id: str,
        org_id: str,
        report_id: str,
    ) -> InvoiceReportResponse:
        """
        Return One Invoice Report

        Returns the status and details of a previously requested invoice report.

        Args:
            invoice_id: Unique string that identifies the invoice the report was generated for.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            report_id: Unique string that identifies the report to retrieve.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/invoices/{quote(str(invoice_id), safe='')}/reports/{quote(str(report_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=InvoiceReportResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def list_skus(
        self,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiSKUView:
        """
        Return All Stock Keeping Units

        Returns all available SKUs (Stock Keeping Units) that can appear on MongoDB invoices. SKUs represent different products and services offered by MongoDB.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/skus"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiSKUView,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_sku(
        self,
        sku_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SkuResponse:
        """
        Return One Stock Keeping Unit

        Returns details about a single SKU (Stock Keeping Unit) by its identifier. SKUs represent different products and services offered by MongoDB.

        Args:
            sku_id: Unique identifier of the SKU to retrieve.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/skus/{quote(str(sku_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=SkuResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
