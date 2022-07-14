import Utils from "../Utils";

export default class {
    /**
     * Create a new RelatedRequest instance.
     */
    constructor(database, model, config) {
        this.database = database;
        this.model = model;
        this.config = config;
        this.relations = [];
    }

    async requestPaths(paths){
        const promises = Array();
        console.log("Paths", paths);
        if(this.relations.length > 0){
            var paths = paths.split(",");
    
            for (let i = 0; i < paths.length; i++) {
                var pathList = paths[i].split(".");
                var pathCaller = this.getCurrentPathCaller(pathList);
                var pathRelation = this.getCurrentPathRelation(pathList);
    
                promises.push(this.requestPathLocation(pathList, pathCaller, pathRelation, this.relations));
            }
        }
        
        return await Promise.all(promises);
    }


    async requestPathLocation(pathList, currentPathCallerEntity, currentPathRelation, relations){
        let currentPathRelationType = this.config.resourceToEntityCase(currentPathRelation);        
        
        for (let i = 0; i < this.relations.length; i++) {
            let isPathCallerEqualModelEntity = currentPathCallerEntity == this.model.entity;
            let isPathRelationEqualRelation = currentPathRelationType == this.relations[i].relatedName;
            
            if(isPathCallerEqualModelEntity && isPathRelationEqualRelation){
                let relatedModel = Utils.modelFor(this.database, relations[i].relatedType);
                
                let options = { 
                    fetchRelated: this.getNextPathString(pathList, relations[i]),
                }
                console.log("Call", this.relations[i].relatedLinks.related.slice(0,-1), options)
                return await relatedModel.jsonApi().get(this.relations[i].relatedLinks.related.slice(0,-1), options);
            }
        }
    }

    addRelation(relation){
        this.relations.push(relation);
    }

    getCurrentPathCaller(pathList){
        return pathList.slice(0,1).toString().slice(1);
    }

    getCurrentPathRelation(pathList){
        return pathList.slice(1,2).toString();
    }

    getCurrentPathRelationEntityName(relation){
        return "#" + relation.relatedType;
    }

    getNextPathString(pathList, relation){

        var cutted = pathList.slice(2);
        console.log(pathList, cutted);
        if(cutted.length >= 1){
            return this.getCurrentPathRelationEntityName(relation) + "." + cutted.join(".");
        }
        return "";
    }
  }
  