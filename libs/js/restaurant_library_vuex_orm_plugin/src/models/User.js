// User Model

import { Model } from '@vuex-orm/core'
import Profile from './Profile'

class User extends Model {
  static entity = 'User'

  static jsonApiConfig = {
    entityToResourceRouteCase: x => "users"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("User"),

      id: this.attr(null),
      username: this.attr(''),
      phone_number: this.attr(''),
      email: this.attr(''),
      password: this.attr(''),
      isAuthenticated: this.boolean(false),
      
      profile: this.hasOne(Profile, 'user_id')
    }
  }
}

const users = {
  namespaced: true,
  actions: {
    loginUser({ commit }, auhorization) {
      let serialized = User.jsonApi().serialize(auhorization)
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/core/log_in/?include=profile",
        scope: (query) => query.with('profile').with('profile.address') 
      }
      return User.jsonApi().post(null, serialized, options);
    },
    logoutUser({ commit }) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/core/log_out"
      }
      return User.jsonApi().get(options.url);
    },
    smsCodeToUser({ commit }, identifier) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/core/user-send-sms-code/",
        headers: { 'Content-Type': 'application/json' }
      }
      var serialized = User.jsonApi().serialize(identifier)
      return User.jsonApi().post(null, serialized, options);
    },
    mailTokenToUser({ commit }, identifier) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/core/user-send-mail-token/",
        headers: { 'Content-Type': 'application/json' }
      }
      var serialized = User.jsonApi().serialize(identifier)
      return User.jsonApi().post(null, serialized, options);
    },
    updatePassword({ commit }, authorizePassword) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/users/" + authorizePassword.id + "/update-password/",
        headers: { 'Content-Type': 'application/json' },
        scope: (query) => query.with('profiley').with('profile.address') 
      }
      var serialized = User.jsonApi().serialize(authorizePassword)
      var t = User.jsonApi().create(serialized, options);
      return t
    },
    updateEmail({ commit }, authorizeEmail) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/users/" + authorizeEmail.id + "/update-email/",
        headers: { 'Content-Type': 'application/json' },
        scope: (query) => query.with('profile.').with('profile.address') 
      }
      var serialized = User.jsonApi().serialize(authorizeEmail)
      return User.jsonApi().post(null, serialized, options);
    },
    updatePhoneNumber({ commit }, authorizePhoneNumber) {
      let options = { 
        url: process.env.VUE_APP_BASE_API_URL + "/users/" + authorizePhoneNumber.id + "/update-phone-number/",
        headers: { 'Content-Type': 'application/json' },
        scope: (query) => query.with('profile').with('profile.address') 
      }
      var serialized = User.jsonApi().serialize(authorizePhoneNumber)
      return User.jsonApi().post(null, serialized, options);
    },
  },
  getters: {
    isAuthenticated(){
      return User.exists()
    },
  }
}

export { User, users }