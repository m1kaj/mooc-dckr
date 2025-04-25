FROM grafana/grafana-oss:latest

ARG GF_GID="0"
ARG GF_INSTALL_PLUGINS="yesoreyeram-infinity-datasource"
ENV GF_PATHS_PLUGINS="/var/lib/grafana-plugins"
ENV GF_USERS_ALLOW_SIGN_UP="false"
ENV GF_SECURITY_ADMIN_USER="docker"
ENV GF_SECURITY_ADMIN_PASSWORD="moocmooc"
ENV GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH="/etc/dashboards/vaesto_ian_mukaan_dashboard.json"

USER root

RUN mkdir -p "$GF_PATHS_PLUGINS" && \
    chown -R grafana:${GF_GID} "$GF_PATHS_PLUGINS"

USER grafana

RUN grafana-cli --pluginsDir "${GF_PATHS_PLUGINS}" plugins install ${GF_INSTALL_PLUGINS}

COPY provision/infinity.yaml /etc/grafana/provisioning/datasources/
COPY provision/vaesto.yaml /etc/grafana/provisioning/dashboards/
COPY provision/vaesto_ian_mukaan_dashboard.json /etc/dashboards/