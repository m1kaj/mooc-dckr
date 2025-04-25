FROM grafana/grafana-oss:latest-ubuntu

ARG GF_GID="0"
ARG GF_INSTALL_PLUGINS="yesoreyeram-infinity-datasource"
ENV GF_PATHS_PLUGINS="/var/lib/grafana-plugins"

USER root

RUN mkdir -p "$GF_PATHS_PLUGINS" && \
    chown -R grafana:${GF_GID} "$GF_PATHS_PLUGINS"

USER grafana

RUN grafana-cli --pluginsDir "${GF_PATHS_PLUGINS}" plugins install ${GF_INSTALL_PLUGINS}
