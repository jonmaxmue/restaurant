import { Model } from '@vuex-orm/core'
import Profile from './Profile'

export default class Address extends Model {
  static entity = 'Address'

  static jsonApiConfig = {
    entityToResourceRouteCase: x => "addresses"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("Address"),

      id: this.attr(null),
      plz: this.attr(''),
      street: this.attr(''),
      house: this.attr(''),
      geo_point: this.attr(''),

      // extra defined foreignkeys for vuex-orm
      profile_id: this.attr(null),
      profile: this.belongsTo(Profile, 'profile_id')   
    }
  }
}