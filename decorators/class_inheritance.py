class Base:
    def __init__(self,**kwargs):
        print("run")
        self.project_id = kwargs.get("project_id")

class InfraData(Base):
    def __init__(self, **kwargs):
        
        pass
       
        




if __name__ =="__main__":
    data = {"project_id":"11472"}
    infra = InfraData(**data)
