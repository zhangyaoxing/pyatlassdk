# Known issues

This file records the issues that remain open after the first regression-fix batch.

Issues **1-4 and 6-8** from the original test-suite branch are fixed in the generator. Their
strict-xfail tests are now normal regression tests in `tests/test_known_issues.py`:

- `Literal[true]` / `Literal[false]` annotations
- resource class shadowing the model it returns
- empty successful responses raising `JSONDecodeError`
- gzip / CSV downloads parsed as JSON
- auth responses that are not JSON objects
- 3xx responses not reported as `AtlasApiError`
- empty `access_token` accepted by the App client

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

## 9. Explicit `None` is never sent as JSON `null` (Note, by design)

`_serialize()` dumps models with `exclude_none=True`, so a field set to `None` is
indistinguishable from an unset field and JSON `null` is never transmitted. APIs that clear a
value by receiving `null` (PATCH-style updates) cannot be driven through the typed models;
passing a raw `dict` as the body is the workaround.

This is intentional behavior, not a defect. If explicit null clearing becomes a requirement,
switch request serialization to `model_dump(mode="json", by_alias=True, exclude_unset=True)`:
that omits fields that were never provided while preserving fields explicitly set to `None`.
The change affects every request body and needs a deliberate decision.

Pinned by the passing characterization test
`test_explicit_none_cannot_be_sent_to_clear_a_field`.

Upstream: <https://github.com/zhangyaoxing/mongo-atlas-sdk/issues/9>

---

## How the suites are organized

| File | Covers |
|------|--------|
| `test_package.py`, `test_errors.py`, `test_enums.py` | public surface, error types, enum helpers |
| `test_serialization.py`, `test_request_pipeline.py` | `_serialize`/`_payload`, `request()` for all 3 clients |
| `test_admin_client.py`, `test_app_client.py`, `test_status_client.py` | construction, Digest/OAuth, login, every status endpoint |
| `test_resource_contract.py` | 715 generated methods x ~12 invariants (verb, quoting, params, body, headers) |
| `test_models.py` | structure of all 1,292 generated model modules, lazy exports |
| `test_known_issues.py` | regression tests for fixed issues and the issue 9 characterization |
