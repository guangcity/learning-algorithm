class RandomizedCollection {

    List<Integer> list = new ArrayList<Integer>();
    Map<Integer, Set<Integer>> map = new HashMap<Integer, Set<Integer>>();

    /** Initialize your data structure here. */
    public RandomizedCollection() {

    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        boolean flag = false;
        Set<Integer> idxs = null;
        if (map.containsKey(val)) {
            idxs = map.get(val);
            flag=false;
        } else {
            idxs = new HashSet<Integer>();
            flag=true;
        }
        idxs.add(list.size());
        list.add(val);
        map.put(val,idxs);
        return flag;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        } else {
            Set<Integer> rmIdxs = map.get(val);
            int rmIdx = rmIdxs.iterator().next();
            if (rmIdx < list.size() - 1&&val!=list.get(list.size()-1)) {

                int lastElem = list.get(list.size() - 1);
                Set<Integer> lastElemIdxs = map.get(lastElem);
                lastElemIdxs.remove(list.size()-1);
                lastElemIdxs.add(rmIdx);
                list.set(rmIdx,lastElem);
                map.put(lastElem,lastElemIdxs);
            }
            if(val == list.get(list.size()-1)){
                rmIdx=list.size()-1;
            }
            rmIdxs.remove(rmIdx);
            if(rmIdxs.size()==0){
                map.remove(val);
            }else{
                map.put(val,rmIdxs);
            }
            list.remove(list.size() - 1);
            return true;
        }
    }

    Random r = new Random();

    /** Get a random element from the collection. */
    public int getRandom() {
        return list.get(r.nextInt(list.size()));
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */