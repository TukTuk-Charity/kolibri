import urls from 'kolibri.urls';
import client from 'kolibri.client';

export default {
  namespaced: true,
  state: {
    deviceInfo: {},
    deviceName: null,
  },
  mutations: {
    SET_STATE(state, payload) {
      state.deviceInfo = payload.deviceInfo;
      state.deviceName = payload.deviceInfo.device_name;
    },
    SET_DEVICE_NAME(state, name) {
      state.deviceName = name;
    },
    RESET_STATE(state) {
      state.deviceInfo = {};
      state.deviceName = null;
    },
  },
  actions: {
    updateDeviceName(store, name) {
      return client({
        path: urls['kolibri:core:devicename'](),
        method: 'PATCH',
        entity: {
          name,
        },
      }).then(response => {
        store.commit('SET_DEVICE_NAME', response.entity.name);
      });
    },
  },
};
