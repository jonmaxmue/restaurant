import { Model } from '@vuex-orm/core'
import Profile from './Profile'

export default class Restaurant extends Model {
  static entity = 'Restaurant'

  static jsonApiConfig = {
    entityToResourceRouteCase: x => "Restaurants"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("Restaurant"),

      id: this.attr(null),
      name: this.attr(''),
    }
  }
}