from hero_management import HeroManagement

import pytest

class Test_Hero:

    def setup_method(self):
        self.hero=HeroManagement()
    """
    增加测试
    """
    #name 等价类测试
    #name 字符串"jinx" volume 1  power 10   -success
    #name 23   volume 1  power 10   -Fail   Flase
    #name True  volume 1 power 10   -Fail  Flase

    @pytest.mark.parametrize("name,volume,power",[("jinx",1,10)])
    def test_create_hero_name_success(self,name,volume,power):     
        self.hero.create_hero(name,volume,power)
        new_name=self.hero.find_hero(name)
        print(new_name)
        assert new_name["name"]==name

    @pytest.mark.parametrize("name,volume,power",[(23,1,10),(True,1,10)])
    def test_create_hero_name_fail(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        try:
            assert flag==False
        except  AssertionError as e:
            print(e)

    
    #test volume 边值分析
    @pytest.mark.parametrize("name,volume,power",[("jinx",0,10)])
    def test_create_hero_voulme_0(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        assert flag==False
    
    @pytest.mark.parametrize("name,volume,power",[("jinx",1,10)])
    def test_create_hero_voulme_1(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        assert flag==True
    @pytest.mark.parametrize("name,volume,power",[("jinx",2,10)])
    def test_create_hero_voulme_2(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        assert flag==True

    @pytest.mark.parametrize("name,volume,power",[("jinx",98,10)])
    def test_create_hero_voulme_98(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        assert flag==True

    @pytest.mark.parametrize("name,volume,power",[("jinx",99,10)])
    def test_create_hero_voulme_99(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        try:
            assert flag==True
        except AssertionError as e:
            print(e)

    @pytest.mark.parametrize("name,volume,power",[("jinx",100,10)])
    def test_create_hero_voulme_100(self,name,volume,power):
        flag=self.hero.create_hero(name,volume,power)
        try:
            assert flag==False
        except AssertionError as e:
            print(e)
    """
    查询测试
    """
    def test_find_hero_no_exist(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.find_hero("")
        assert res ==False

    def test_find_hero_exist(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.find_hero("jinx")
        assert res["name"] =="jinx"
    """
    修改测试
    """
    def test_update_hero_exist(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.update_hero("jinx",99)
        assert res["volume"]==99
    

    def test_update_hero_no_exist(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.update_hero("abc",99)
        assert res==False
    """
    删除测试
    """
    def test_delete_hero_exist(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.delete_hero("jinx")
        assert len(res)==0
    
    def test_delete_hero_exist_no(self):
        self.hero.create_hero("jinx",1,100)
        res=self.hero.delete_hero("abc")
        assert res==False
        



if __name__=="__main__":
    pytest.main()