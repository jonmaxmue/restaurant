// Profile Model

import { Model } from '@vuex-orm/core'
import Address from './Address'
import { User } from './User'

export default class Profile extends Model {
  static entity = 'Profile'
  
  static jsonApiConfig = {
    entityToResourceRouteCase: x => "profiles"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("Profile"),


      id: this.attr(null),
      firstname: this.attr(''),
      lastname: this.attr(''),
      date_of_birth: this.attr(''),
      avatar: this.attr(''),
      is_preacher: this.attr(''),
      age: this.attr(''),
      gender: this.attr(''),
      created: this.attr(''),
      username: this.attr(''),

      address: this.hasOne(Address, 'profile_id'),

      user_id: this.attr(null),
      user: this.belongsTo(User, 'user_id')   
    }
  }
}

const profiles = {
  namespaced: true,
  actions: {
    
  },
  getters: {

  }
}

export { Profile, profiles }