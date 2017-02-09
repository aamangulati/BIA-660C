  

    def min(self,col_name):
        nums ,is_time= self.transform_type(col_name)
        result = min(nums)
        return datetime.datetime.fromtimestamp(result) if is_time else result

    def max(self,col_name):
        nums, is_time = self.transform_type(col_name)
        result = max(nums)
        return datetime.datetime.fromtimestamp(result) if is_time else result

    def median(self,col_name):
        nums, is_time = self.transform_type(col_name)
        nums = sorted(nums)
        center = int(len(nums) / 2)
        if len(nums) % 2 == 0:
            result = sum(nums[center - 1:center + 1]) / 2.0
            return datetime.datetime.fromtimestamp(result) if is_time else result
        else:
            result = nums[center]
            return datetime.datetime.fromtimestamp(result) if is_time else result

    def mean(self,col_name):
        nums, is_time = self.transform_type(col_name)
        result = sum(nums)/len(nums)
        return datetime.datetime.fromtimestamp(rslt) if is_time else result

    
    def sum(self,col_name):
        nums,is_time = self.transform_type(col_name)
        return sum(nums)

    def std(self,col_name):
        nums ,is_time = self.transform_type(col_name)
        mean = sum(nums)/len(nums)
        return (sum([(num-mean)**2 for num in nums])/len(nums))**0.5

    def get_rows_where_column_has_value(self, column_name, value, index_only=False):
        if index_only:
            return [index for index, row_value in enumerate(self[column_name]) if row_value==value]
        else:
            return [row for row in self.data if row[column_name]==value]
