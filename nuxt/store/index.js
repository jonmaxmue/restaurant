import {
  VuexORM,
  Database,
  User,
  users,
  Profile,
  profiles,
  Address,
  Restaurant,
  Table,
  Seat
} from '@restaurant-dev/vuex-orm'


Database.register(User, users)
Database.register(Profile, profiles)
Database.register(Address)
Database.register(Restaurant)
Database.register(Table)
Database.register(Seat)

const VuexORMPlugin = VuexORM.install(Database)

export const plugins = [VuexORMPlugin]

