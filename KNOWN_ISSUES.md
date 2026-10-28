# Known issues

This file records the issues that remain open after the regression-fix batch.

Issues **1-4 and 6-9** from the original test-suite branch are fixed in the generator. Their
strict-xfail tests are now normal regression tests in `tests/test_known_issues.py`:

- `Literal[true]` / `Literal[false]` annotations
- resource class shadowing the model it returns
- empty successful responses raising `JSONDecodeError`
- gzip / CSV downloads parsed as JSON
- auth responses that are not JSON objects
- 3xx responses not reported as `AtlasApiError`
- empty `access_token` accepted by the App client
- explicit `None` values now serialize as JSON `null`; unset fields are omitted

Tracked upstream in <https://github.com/zhangyaoxing/mongo-atlas-sdk/issues>.

---

## 5. `GET` sent with a JSON body (Medium, spec-defined)

`invoices.search_org_invoice_line_items` (`.../invoices/{invoiceId}/lineItems:search`) issues
`GET` with a JSON body. This is unusual because bodies on `GET` are not portable, but it matches
the current official Atlas Admin API v2 OpenAPI document:

```text
METHOD GET
operationId: searchOrgInvoiceLineItems
requestBody: true
```

The generated method therefore accurately reflects the spec. No generator change is planned
unless Atlas changes the OpenAPI document.

Test: `test_resource_contract.py::test_get_requests_have_no_body` keeps a strict xfail for this
single endpoint so the exception remains visible.

Upstream: <https://github.com/zhangyaoxing/mongo-atlas-sdk/issues/5>

---

## How the suites are organized

| File | Covers |
|------|--------|
| `test_package.py`, `test_errors.py`, `test_enums.py` | public surface, error types, enum helpers |
| `test_serialization.py`, `test_request_pipeline.py` | `_serialize`/`_payload`, `request()` for all 3 clients |
| `test_admin_client.py`, `test_app_client.py`, `test_status_client.py` | construction, Digest/OAuth, login, every status endpoint |
| `test_resource_contract.py` | 715 generated methods x ~12 invariants (verb, quoting, params, body, headers) |
| `test_models.py` | structure of all 1,292 generated model modules, lazy exports |
| `test_known_issues.py` | regression tests for fixed issues |
