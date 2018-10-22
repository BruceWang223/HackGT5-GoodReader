const state = {
	resData: {},
	isloading: false
}

export const actions = {
	setResData ({ commit }, data) {
		commit('setData', data);
	},
	getResData ({ commit }, data) {
		commit('getData', data);
	},
	setLoading ({ commit }, isloading) {
		commit('setLoading', isloading);
	}
};

const mutations = {
	setData(state, data) {
		state.resData = data;
		console.log(state.resData);
		state.isloading = false;
	},
	getData(state, data) {
		data = state.resData;
	},
	setLoading(state, isloading) {
		state.isloading = isloading;
	}
};

const getters = {
	resData: state => {
		console.log(state.resData);
		return state.resData;
	}
}

export const dataModule = {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};