# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ATROPOS_METADATA = Metadata(
    id="4cb469cdce62fc57298fef68a491750d55ea4517.boutiques",
    name="Atropos",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


AtroposParameters = typing.TypedDict('AtroposParameters', {
    "__STYXTYPE__": typing.Literal["Atropos"],
    "image_dimensionality": typing.NotRequired[typing.Literal[2, 3, 4] | None],
    "intensity_image": str,
    "bspline": typing.NotRequired[str | None],
    "initialization": str,
    "partial_volume_label_set": typing.NotRequired[str | None],
    "use_partial_volume_likelihoods": typing.NotRequired[typing.Literal[0, 1] | None],
    "posterior_formulation": typing.NotRequired[str | None],
    "mask_image": InputPathType,
    "convergence": str,
    "likelihood_model": str,
    "mrf": typing.NotRequired[str | None],
    "icm": typing.NotRequired[str | None],
    "use_random_seed": typing.NotRequired[typing.Literal[0, 1] | None],
    "output": str,
    "minimize_memory_usage": typing.NotRequired[typing.Literal[0, 1] | None],
    "winsorize_outliers": typing.NotRequired[str | None],
    "use_euclidean_distance": typing.NotRequired[typing.Literal[0, 1] | None],
    "label_propagation": typing.NotRequired[str | None],
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "Atropos": atropos_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "Atropos": atropos_outputs,
    }.get(t)


class AtroposOutputs(typing.NamedTuple):
    """
    Output object returned when calling `atropos(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    classified_image: OutputPathType
    """The output labeled image with assigned labels for each voxel in the
    masked region."""
    posterior_probability_images: OutputPathType
    """Output posterior probability images in specified format."""


def atropos_params(
    intensity_image: str,
    initialization: str,
    mask_image: InputPathType,
    convergence: str,
    likelihood_model: str,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    bspline: str | None = None,
    partial_volume_label_set: str | None = None,
    use_partial_volume_likelihoods: typing.Literal[0, 1] | None = None,
    posterior_formulation: str | None = None,
    mrf: str | None = None,
    icm: str | None = None,
    use_random_seed: typing.Literal[0, 1] | None = None,
    minimize_memory_usage: typing.Literal[0, 1] | None = None,
    winsorize_outliers: str | None = None,
    use_euclidean_distance: typing.Literal[0, 1] | None = None,
    label_propagation: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> AtroposParameters:
    """
    Build parameters.
    
    Args:
        intensity_image: One or more scalar images is specified for\
            segmentation. For scenarios with no prior information, the first scalar\
            image is used to order labelings by intensity. The optional adaptive\
            smoothing weight is applicable with prior images, specified between\
            [0,1].
        initialization: Initialize the FMM parameters. options include Random,\
            Otsu, KMeans, PriorProbabilityImages, and PriorLabelImage.
        mask_image: The required image mask defines the region to be labeled by\
            Atropos.
        convergence: Determine convergence based on mean maximum posterior\
            probability over region of interest.
        likelihood_model: Specify parametric or non-parametric likelihood\
            model. Options include Gaussian, HistogramParzenWindows,\
            ManifoldParzenWindows, among others.
        output: Output labeled image and optionally posterior probability\
            images.
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, Atropos tries to infer\
            the dimensionality from the first input image.
        bspline: Parameters for B-Spline. Adaptive smoothing is applied to\
            intensity images if smoothing weights > 0.
        partial_volume_label_set: Model mixtures of classes within single\
            voxels. Specify labels for each partial volume class.
        use_partial_volume_likelihoods: Whether to use partial volume\
            likelihoods. A value of 1 considers the partial volume class separate\
            from tissue classes.
        posterior_formulation: Specify posterior probability formulation.\
            Options are Socrates, Plato, Aristotle, or Sigmoid.
        mrf: Markov Random Field parameters to enforce spatial constraints on\
            segmentation.
        icm: ICM (Iterated Conditional Modes) parameters for asynchronous\
            updating.
        use_random_seed: Initialize with a random seed or a constant seed\
            number.
        minimize_memory_usage: Minimize memory usage by calculating images on\
            the fly and storing only non-negligible pixel values.
        winsorize_outliers: Options to remove effects of outliers in\
            calculations using methods like BoxPlot or GrubbsRosner.
        use_euclidean_distance: Propagate labels throughout the mask using a\
            distance transform.
        label_propagation: Control propagation of each prior label by specified\
            lambda and boundary probability.
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "Atropos",
        "intensity_image": intensity_image,
        "initialization": initialization,
        "mask_image": mask_image,
        "convergence": convergence,
        "likelihood_model": likelihood_model,
        "output": output,
    }
    if image_dimensionality is not None:
        params["image_dimensionality"] = image_dimensionality
    if bspline is not None:
        params["bspline"] = bspline
    if partial_volume_label_set is not None:
        params["partial_volume_label_set"] = partial_volume_label_set
    if use_partial_volume_likelihoods is not None:
        params["use_partial_volume_likelihoods"] = use_partial_volume_likelihoods
    if posterior_formulation is not None:
        params["posterior_formulation"] = posterior_formulation
    if mrf is not None:
        params["mrf"] = mrf
    if icm is not None:
        params["icm"] = icm
    if use_random_seed is not None:
        params["use_random_seed"] = use_random_seed
    if minimize_memory_usage is not None:
        params["minimize_memory_usage"] = minimize_memory_usage
    if winsorize_outliers is not None:
        params["winsorize_outliers"] = winsorize_outliers
    if use_euclidean_distance is not None:
        params["use_euclidean_distance"] = use_euclidean_distance
    if label_propagation is not None:
        params["label_propagation"] = label_propagation
    if verbose is not None:
        params["verbose"] = verbose
    return params


def atropos_cargs(
    params: AtroposParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("Atropos")
    if params.get("image_dimensionality") is not None:
        cargs.extend([
            "--image-dimensionality",
            str(params.get("image_dimensionality"))
        ])
    cargs.extend([
        "-a",
        params.get("intensity_image")
    ])
    if params.get("bspline") is not None:
        cargs.extend([
            "-b",
            params.get("bspline")
        ])
    cargs.extend([
        "-i",
        params.get("initialization")
    ])
    if params.get("partial_volume_label_set") is not None:
        cargs.extend([
            "-s",
            params.get("partial_volume_label_set")
        ])
    if params.get("use_partial_volume_likelihoods") is not None:
        cargs.extend([
            "--use-partial-volume-likelihoods",
            str(params.get("use_partial_volume_likelihoods"))
        ])
    if params.get("posterior_formulation") is not None:
        cargs.extend([
            "-p",
            params.get("posterior_formulation")
        ])
    cargs.extend([
        "-x",
        execution.input_file(params.get("mask_image"))
    ])
    cargs.extend([
        "-c",
        params.get("convergence")
    ])
    cargs.extend([
        "-k",
        params.get("likelihood_model")
    ])
    if params.get("mrf") is not None:
        cargs.extend([
            "-m",
            params.get("mrf")
        ])
    if params.get("icm") is not None:
        cargs.extend([
            "-g",
            params.get("icm")
        ])
    if params.get("use_random_seed") is not None:
        cargs.extend([
            "-r",
            str(params.get("use_random_seed"))
        ])
    cargs.extend([
        "-o",
        params.get("output")
    ])
    if params.get("minimize_memory_usage") is not None:
        cargs.extend([
            "-u",
            str(params.get("minimize_memory_usage"))
        ])
    if params.get("winsorize_outliers") is not None:
        cargs.extend([
            "-w",
            params.get("winsorize_outliers")
        ])
    if params.get("use_euclidean_distance") is not None:
        cargs.extend([
            "-e",
            str(params.get("use_euclidean_distance"))
        ])
    if params.get("label_propagation") is not None:
        cargs.extend([
            "-l",
            params.get("label_propagation")
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose"))
        ])
    return cargs


def atropos_outputs(
    params: AtroposParameters,
    execution: Execution,
) -> AtroposOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AtroposOutputs(
        root=execution.output_file("."),
        classified_image=execution.output_file(params.get("output") + "_classified.nii.gz"),
        posterior_probability_images=execution.output_file("[POSTERIOR_PROBABILITY_IMAGE_FILE_NAME_FORMAT]"),
    )
    return ret


def atropos_execute(
    params: AtroposParameters,
    execution: Execution,
) -> AtroposOutputs:
    """
    Atropos is a finite mixture modeling (FMM) segmentation approach that allows for
    prior constraints including a prior label image, prior probability images,
    and/or an MRF prior to enforce spatial smoothing of the labels.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AtroposOutputs`).
    """
    params = execution.params(params)
    cargs = atropos_cargs(params, execution)
    ret = atropos_outputs(params, execution)
    execution.run(cargs)
    return ret


def atropos(
    intensity_image: str,
    initialization: str,
    mask_image: InputPathType,
    convergence: str,
    likelihood_model: str,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    bspline: str | None = None,
    partial_volume_label_set: str | None = None,
    use_partial_volume_likelihoods: typing.Literal[0, 1] | None = None,
    posterior_formulation: str | None = None,
    mrf: str | None = None,
    icm: str | None = None,
    use_random_seed: typing.Literal[0, 1] | None = None,
    minimize_memory_usage: typing.Literal[0, 1] | None = None,
    winsorize_outliers: str | None = None,
    use_euclidean_distance: typing.Literal[0, 1] | None = None,
    label_propagation: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AtroposOutputs:
    """
    Atropos is a finite mixture modeling (FMM) segmentation approach that allows for
    prior constraints including a prior label image, prior probability images,
    and/or an MRF prior to enforce spatial smoothing of the labels.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        intensity_image: One or more scalar images is specified for\
            segmentation. For scenarios with no prior information, the first scalar\
            image is used to order labelings by intensity. The optional adaptive\
            smoothing weight is applicable with prior images, specified between\
            [0,1].
        initialization: Initialize the FMM parameters. options include Random,\
            Otsu, KMeans, PriorProbabilityImages, and PriorLabelImage.
        mask_image: The required image mask defines the region to be labeled by\
            Atropos.
        convergence: Determine convergence based on mean maximum posterior\
            probability over region of interest.
        likelihood_model: Specify parametric or non-parametric likelihood\
            model. Options include Gaussian, HistogramParzenWindows,\
            ManifoldParzenWindows, among others.
        output: Output labeled image and optionally posterior probability\
            images.
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, Atropos tries to infer\
            the dimensionality from the first input image.
        bspline: Parameters for B-Spline. Adaptive smoothing is applied to\
            intensity images if smoothing weights > 0.
        partial_volume_label_set: Model mixtures of classes within single\
            voxels. Specify labels for each partial volume class.
        use_partial_volume_likelihoods: Whether to use partial volume\
            likelihoods. A value of 1 considers the partial volume class separate\
            from tissue classes.
        posterior_formulation: Specify posterior probability formulation.\
            Options are Socrates, Plato, Aristotle, or Sigmoid.
        mrf: Markov Random Field parameters to enforce spatial constraints on\
            segmentation.
        icm: ICM (Iterated Conditional Modes) parameters for asynchronous\
            updating.
        use_random_seed: Initialize with a random seed or a constant seed\
            number.
        minimize_memory_usage: Minimize memory usage by calculating images on\
            the fly and storing only non-negligible pixel values.
        winsorize_outliers: Options to remove effects of outliers in\
            calculations using methods like BoxPlot or GrubbsRosner.
        use_euclidean_distance: Propagate labels throughout the mask using a\
            distance transform.
        label_propagation: Control propagation of each prior label by specified\
            lambda and boundary probability.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AtroposOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ATROPOS_METADATA)
    params = atropos_params(
        image_dimensionality=image_dimensionality,
        intensity_image=intensity_image,
        bspline=bspline,
        initialization=initialization,
        partial_volume_label_set=partial_volume_label_set,
        use_partial_volume_likelihoods=use_partial_volume_likelihoods,
        posterior_formulation=posterior_formulation,
        mask_image=mask_image,
        convergence=convergence,
        likelihood_model=likelihood_model,
        mrf=mrf,
        icm=icm,
        use_random_seed=use_random_seed,
        output=output,
        minimize_memory_usage=minimize_memory_usage,
        winsorize_outliers=winsorize_outliers,
        use_euclidean_distance=use_euclidean_distance,
        label_propagation=label_propagation,
        verbose=verbose,
    )
    return atropos_execute(params, execution)


__all__ = [
    "ATROPOS_METADATA",
    "AtroposOutputs",
    "AtroposParameters",
    "atropos",
    "atropos_params",
]
