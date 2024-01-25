from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
     * `DeclarativeBase` is inherited only once throughout whole project to create 'base class'
     * According to document, this class 'apply the declarative mapping process to all subclasses that derive from it'
     * Therefore, any class that defines data model in the DB should inherit this class
     * FYI: can have any name as a developer wants

     Reference : https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#orm-declarative-mapping
    """
    pass
