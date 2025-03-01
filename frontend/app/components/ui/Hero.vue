<template>
	<div class="hero min-h-screen bg-base-200">
		<div class="hero-content flex-col lg:flex-row-reverse">
			<div class="text-center lg:text-left">
				<slot name="contentRight" />
			</div>
			<slot />
		</div>
	</div>
</template>
