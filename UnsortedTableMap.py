from abc import ABCMeta, abstractmethod
from collections import MutableMapping
class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key=k
            self._value=v

        def __eq__(self, other): #key가 같으냐
            return self._key==other._key

        def __ne__(self, other): #다르냐
            return not (self==other)

        def __lt__(self, other): #다른 키보다 작느냐
            return self._key<other._key

class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table=[]

    def __getitem__(self, k):
        for item in self._table:
            if k==item._key:
                return item._value
        raise KeyError('KeyError'+repr(k)) #repr은 공식적인 문자열을 출력 for 개발자

    def __setitem__(self, k,v):
        for item in self._table:
            if item._key == k:
                item._value=v
                return

        self._table.append(self._Item(k,v))

    def _delitem__(self,k):
        for j in range(len(self._table)):
            if self._table[j]._key==k:
                self._table.pop(j)
                return
        raise KeyError('KeyError'+repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key #key의 generator을 반환