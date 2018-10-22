import Vue from 'vue';
import Vuex from 'vuex';

import { dataModule } from './data.module';

Vue.use(Vuex);

export const store = new Vuex.Store({
	modules: {
		dataModule
	}
});
