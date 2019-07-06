# Goals

- Update the `manifest.json` file.
- Update the `metadata.csv` file.
- Update the `service_checks.json` file.
- Update the `README.md` file.
- Create a wheel, install and configure the integration.
- Make sure metrics are being submitted to your datadog account.  

# Hints

- See `manifest.json` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#manifest-file).
- See `metadata.csv` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#metrics-metadata-file).
- See `service_checks.json` [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#service-check-file).
- See [documentation](https://docs.datadoghq.com/developers/integrations/new_check_howto/#building) to build and install an integration.
- See Agent [documentation](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/?tab=agentv6#commands) to see agent commands.
  - Use the `check` command to make sure you integration runs correctly.
 