import Utils from "../Utils";

export default class {
    /**
     * Create a new RelatedRequest instance.
     */
    constructor(relatedName, relatedType, relatedLinks) {
        this.relatedName = relatedName;
        this.relatedType = relatedType;
        this.relatedLinks = relatedLinks;
    }

    /*
    async raequestRelations(levels){
        let type = this.resourceToEntityCase(this.type);        
        
        if(levels[0] == this.model.entity && this.relationName == levels[1]){
            let relatedModel = Utils.modelFor(this.database, type);
            
            let options = { 
                fetchRelated: levels.slice(1).join("."),
            }

            await relatedModel.jsonApi().get(this.links.related.slice(0,-1), options);
        }
    }
    */
  }
  