require "base64"

["535970uDvTHu", "5ECSbGl", "1513736WNNtai", "7eFrnBe", "4VeyLTV", "1265955JAKrQv", "2023144Cybidw", "732570GTyzSF", "1718667oVoRBk", "66bKWvOd", "396576Yfzhtz"].permutation.map do |p|
	begin
		puts Base64.decode64(p.join)
	rescue

	end
end