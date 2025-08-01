# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DWI2FOD_METADATA = Metadata(
    id="f90ba900231375ab5ce1f13e4939fae9c3c04d95.boutiques",
    name="dwi2fod",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Dwi2fodFslgradParameters = typing.TypedDict('Dwi2fodFslgradParameters', {
    "__STYXTYPE__": typing.Literal["fslgrad"],
    "bvecs": InputPathType,
    "bvals": InputPathType,
})


Dwi2fodVariousStringParameters = typing.TypedDict('Dwi2fodVariousStringParameters', {
    "__STYXTYPE__": typing.Literal["VariousString"],
    "obj": str,
})


Dwi2fodVariousFileParameters = typing.TypedDict('Dwi2fodVariousFileParameters', {
    "__STYXTYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})


Dwi2fodConfigParameters = typing.TypedDict('Dwi2fodConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Dwi2fodResponseOdfParameters = typing.TypedDict('Dwi2fodResponseOdfParameters', {
    "__STYXTYPE__": typing.Literal["response_odf"],
    "response": InputPathType,
    "odf": str,
})


Dwi2fodParameters = typing.TypedDict('Dwi2fodParameters', {
    "__STYXTYPE__": typing.Literal["dwi2fod"],
    "grad": typing.NotRequired[InputPathType | None],
    "fslgrad": typing.NotRequired[Dwi2fodFslgradParameters | None],
    "shells": typing.NotRequired[list[float] | None],
    "directions": typing.NotRequired[InputPathType | None],
    "lmax": typing.NotRequired[list[int] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "filter": typing.NotRequired[InputPathType | None],
    "neg_lambda": typing.NotRequired[float | None],
    "norm_lambda": typing.NotRequired[float | None],
    "threshold": typing.NotRequired[float | None],
    "niter": typing.NotRequired[int | None],
    "norm_lambda_1": typing.NotRequired[float | None],
    "neg_lambda_1": typing.NotRequired[float | None],
    "predicted_signal": typing.NotRequired[str | None],
    "strides": typing.NotRequired[typing.Union[Dwi2fodVariousStringParameters, Dwi2fodVariousFileParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Dwi2fodConfigParameters] | None],
    "help": bool,
    "version": bool,
    "algorithm": str,
    "dwi": InputPathType,
    "response_odf": list[Dwi2fodResponseOdfParameters],
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
        "dwi2fod": dwi2fod_cargs,
        "fslgrad": dwi2fod_fslgrad_cargs,
        "VariousString": dwi2fod_various_string_cargs,
        "VariousFile": dwi2fod_various_file_cargs,
        "config": dwi2fod_config_cargs,
        "response_odf": dwi2fod_response_odf_cargs,
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
        "dwi2fod": dwi2fod_outputs,
        "response_odf": dwi2fod_response_odf_outputs,
    }.get(t)


def dwi2fod_fslgrad_params(
    bvecs: InputPathType,
    bvals: InputPathType,
) -> Dwi2fodFslgradParameters:
    """
    Build parameters.
    
    Args:
        bvecs: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvals: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslgrad",
        "bvecs": bvecs,
        "bvals": bvals,
    }
    return params


def dwi2fod_fslgrad_cargs(
    params: Dwi2fodFslgradParameters,
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
    cargs.append("-fslgrad")
    cargs.append(execution.input_file(params.get("bvecs")))
    cargs.append(execution.input_file(params.get("bvals")))
    return cargs


def dwi2fod_various_string_params(
    obj: str,
) -> Dwi2fodVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def dwi2fod_various_string_cargs(
    params: Dwi2fodVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def dwi2fod_various_file_params(
    obj: InputPathType,
) -> Dwi2fodVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def dwi2fod_various_file_cargs(
    params: Dwi2fodVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def dwi2fod_config_params(
    key: str,
    value: str,
) -> Dwi2fodConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def dwi2fod_config_cargs(
    params: Dwi2fodConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class Dwi2fodResponseOdfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `list[Dwi2fodResponseOdfParameters](...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    odf: OutputPathType
    """output ODF image"""


def dwi2fod_response_odf_params(
    response: InputPathType,
    odf: str,
) -> Dwi2fodResponseOdfParameters:
    """
    Build parameters.
    
    Args:
        response: input tissue response.
        odf: output ODF image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "response_odf",
        "response": response,
        "odf": odf,
    }
    return params


def dwi2fod_response_odf_cargs(
    params: Dwi2fodResponseOdfParameters,
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
    cargs.append(execution.input_file(params.get("response")))
    cargs.append(params.get("odf"))
    return cargs


def dwi2fod_response_odf_outputs(
    params: Dwi2fodResponseOdfParameters,
    execution: Execution,
) -> Dwi2fodResponseOdfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dwi2fodResponseOdfOutputs(
        root=execution.output_file("."),
        odf=execution.output_file(params.get("odf")),
    )
    return ret


class Dwi2fodOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwi2fod(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    predicted_signal: OutputPathType | None
    """output the predicted dwi image. """
    response_odf: list[Dwi2fodResponseOdfOutputs]
    """Outputs from `dwi2fod_response_odf_outputs`.This is a list of outputs
    with the same length and order as the inputs."""


def dwi2fod_params(
    algorithm: str,
    dwi: InputPathType,
    response_odf: list[Dwi2fodResponseOdfParameters],
    grad: InputPathType | None = None,
    fslgrad: Dwi2fodFslgradParameters | None = None,
    shells: list[float] | None = None,
    directions: InputPathType | None = None,
    lmax: list[int] | None = None,
    mask: InputPathType | None = None,
    filter_: InputPathType | None = None,
    neg_lambda: float | None = None,
    norm_lambda: float | None = None,
    threshold: float | None = None,
    niter: int | None = None,
    norm_lambda_1: float | None = None,
    neg_lambda_1: float | None = None,
    predicted_signal: str | None = None,
    strides: typing.Union[Dwi2fodVariousStringParameters, Dwi2fodVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2fodConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Dwi2fodParameters:
    """
    Build parameters.
    
    Args:
        algorithm: the algorithm to use for FOD estimation. (options are:\
            csd,msmt_csd).
        dwi: the input diffusion-weighted image.
        response_odf: pairs of input tissue response and output ODF images.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        shells: specify one or more b-values to use during processing, as a\
            comma-separated list of the desired approximate b-values (b-values are\
            clustered to allow for small deviations). Note that some commands are\
            incompatible with multiple b-values, and will report an error if more\
            than one b-value is provided.\
            WARNING: note that, even though the b=0 volumes are never referred\
            to as shells in the literature, they still have to be explicitly\
            included in the list of b-values as provided to the -shell option!\
            Several algorithms which include the b=0 volumes in their\
            computations may otherwise return an undesired result.
        directions: specify the directions over which to apply the\
            non-negativity constraint (by default, the built-in 300 direction set\
            is used). These should be supplied as a text file containing [ az el ]\
            pairs for the directions.
        lmax: the maximum spherical harmonic order for the output FOD(s).For\
            algorithms with multiple outputs, this should be provided as a\
            comma-separated list of integers, one for each output image; for\
            single-output algorithms, only a single integer should be provided. If\
            omitted, the command will use the lmax of the corresponding response\
            function (i.e based on its number of coefficients), up to a maximum of\
            8.
        mask: only perform computation within the specified binary brain mask\
            image.
        filter_: the linear frequency filtering parameters used for the initial\
            linear spherical deconvolution step (default = [ 1 1 1 0 0 ]). These\
            should be supplied as a text file containing the filtering coefficients\
            for each even harmonic order.
        neg_lambda: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1).
        norm_lambda: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default = 1).
        threshold: the threshold below which the amplitude of the FOD is\
            assumed to be zero, expressed as an absolute amplitude (default = 0).
        niter: the maximum number of iterations to perform for each voxel\
            (default = 50). Use '-niter 0' for a linear unconstrained spherical\
            deconvolution.
        norm_lambda_1: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default =\
            1e-10).
        neg_lambda_1: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1e-10).
        predicted_signal: output the predicted dwi image.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dwi2fod",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "algorithm": algorithm,
        "dwi": dwi,
        "response_odf": response_odf,
    }
    if grad is not None:
        params["grad"] = grad
    if fslgrad is not None:
        params["fslgrad"] = fslgrad
    if shells is not None:
        params["shells"] = shells
    if directions is not None:
        params["directions"] = directions
    if lmax is not None:
        params["lmax"] = lmax
    if mask is not None:
        params["mask"] = mask
    if filter_ is not None:
        params["filter"] = filter_
    if neg_lambda is not None:
        params["neg_lambda"] = neg_lambda
    if norm_lambda is not None:
        params["norm_lambda"] = norm_lambda
    if threshold is not None:
        params["threshold"] = threshold
    if niter is not None:
        params["niter"] = niter
    if norm_lambda_1 is not None:
        params["norm_lambda_1"] = norm_lambda_1
    if neg_lambda_1 is not None:
        params["neg_lambda_1"] = neg_lambda_1
    if predicted_signal is not None:
        params["predicted_signal"] = predicted_signal
    if strides is not None:
        params["strides"] = strides
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dwi2fod_cargs(
    params: Dwi2fodParameters,
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
    cargs.append("dwi2fod")
    if params.get("grad") is not None:
        cargs.extend([
            "-grad",
            execution.input_file(params.get("grad"))
        ])
    if params.get("fslgrad") is not None:
        cargs.extend(dyn_cargs(params.get("fslgrad")["__STYXTYPE__"])(params.get("fslgrad"), execution))
    if params.get("shells") is not None:
        cargs.extend([
            "-shells",
            ",".join(map(str, params.get("shells")))
        ])
    if params.get("directions") is not None:
        cargs.extend([
            "-directions",
            execution.input_file(params.get("directions"))
        ])
    if params.get("lmax") is not None:
        cargs.extend([
            "-lmax",
            ",".join(map(str, params.get("lmax")))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("filter") is not None:
        cargs.extend([
            "-filter",
            execution.input_file(params.get("filter"))
        ])
    if params.get("neg_lambda") is not None:
        cargs.extend([
            "-neg_lambda",
            str(params.get("neg_lambda"))
        ])
    if params.get("norm_lambda") is not None:
        cargs.extend([
            "-norm_lambda",
            str(params.get("norm_lambda"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
    if params.get("niter") is not None:
        cargs.extend([
            "-niter",
            str(params.get("niter"))
        ])
    if params.get("norm_lambda_1") is not None:
        cargs.extend([
            "-norm_lambda",
            str(params.get("norm_lambda_1"))
        ])
    if params.get("neg_lambda_1") is not None:
        cargs.extend([
            "-neg_lambda",
            str(params.get("neg_lambda_1"))
        ])
    if params.get("predicted_signal") is not None:
        cargs.extend([
            "-predicted_signal",
            params.get("predicted_signal")
        ])
    if params.get("strides") is not None:
        cargs.extend([
            "-strides",
            *dyn_cargs(params.get("strides")["__STYXTYPE__"])(params.get("strides"), execution)
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(params.get("algorithm"))
    cargs.append(execution.input_file(params.get("dwi")))
    cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("response_odf")] for a in c])
    return cargs


def dwi2fod_outputs(
    params: Dwi2fodParameters,
    execution: Execution,
) -> Dwi2fodOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dwi2fodOutputs(
        root=execution.output_file("."),
        predicted_signal=execution.output_file(params.get("predicted_signal")) if (params.get("predicted_signal") is not None) else None,
        response_odf=[dyn_outputs(i["__STYXTYPE__"])(i, execution) if dyn_outputs(i["__STYXTYPE__"]) else None for i in params.get("response_odf")],
    )
    return ret


def dwi2fod_execute(
    params: Dwi2fodParameters,
    execution: Execution,
) -> Dwi2fodOutputs:
    """
    Estimate fibre orientation distributions from diffusion data using spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    * If using csd algorithm:
    Tournier, J.-D.; Calamante, F. & Connelly, A. Robust determination of the
    fibre orientation distribution in diffusion MRI: Non-negativity constrained
    super-resolved spherical deconvolution. NeuroImage, 2007, 35, 1459-1472
    
    * If using msmt_csd algorithm:
    Jeurissen, B; Tournier, J-D; Dhollander, T; Connelly, A & Sijbers, J.
    Multi-tissue constrained spherical deconvolution for improved analysis of
    multi-shell diffusion MRI data. NeuroImage, 2014, 103, 411-426
    
    Tournier, J.-D.; Calamante, F., Gadian, D.G. & Connelly, A. Direct
    estimation of the fiber orientation density function from diffusion-weighted
    MRI data using spherical deconvolution. NeuroImage, 2004, 23, 1176-1185.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Dwi2fodOutputs`).
    """
    params = execution.params(params)
    cargs = dwi2fod_cargs(params, execution)
    ret = dwi2fod_outputs(params, execution)
    execution.run(cargs)
    return ret


def dwi2fod(
    algorithm: str,
    dwi: InputPathType,
    response_odf: list[Dwi2fodResponseOdfParameters],
    grad: InputPathType | None = None,
    fslgrad: Dwi2fodFslgradParameters | None = None,
    shells: list[float] | None = None,
    directions: InputPathType | None = None,
    lmax: list[int] | None = None,
    mask: InputPathType | None = None,
    filter_: InputPathType | None = None,
    neg_lambda: float | None = None,
    norm_lambda: float | None = None,
    threshold: float | None = None,
    niter: int | None = None,
    norm_lambda_1: float | None = None,
    neg_lambda_1: float | None = None,
    predicted_signal: str | None = None,
    strides: typing.Union[Dwi2fodVariousStringParameters, Dwi2fodVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2fodConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Dwi2fodOutputs:
    """
    Estimate fibre orientation distributions from diffusion data using spherical
    deconvolution.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    * If using csd algorithm:
    Tournier, J.-D.; Calamante, F. & Connelly, A. Robust determination of the
    fibre orientation distribution in diffusion MRI: Non-negativity constrained
    super-resolved spherical deconvolution. NeuroImage, 2007, 35, 1459-1472
    
    * If using msmt_csd algorithm:
    Jeurissen, B; Tournier, J-D; Dhollander, T; Connelly, A & Sijbers, J.
    Multi-tissue constrained spherical deconvolution for improved analysis of
    multi-shell diffusion MRI data. NeuroImage, 2014, 103, 411-426
    
    Tournier, J.-D.; Calamante, F., Gadian, D.G. & Connelly, A. Direct
    estimation of the fiber orientation density function from diffusion-weighted
    MRI data using spherical deconvolution. NeuroImage, 2004, 23, 1176-1185.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        algorithm: the algorithm to use for FOD estimation. (options are:\
            csd,msmt_csd).
        dwi: the input diffusion-weighted image.
        response_odf: pairs of input tissue response and output ODF images.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        shells: specify one or more b-values to use during processing, as a\
            comma-separated list of the desired approximate b-values (b-values are\
            clustered to allow for small deviations). Note that some commands are\
            incompatible with multiple b-values, and will report an error if more\
            than one b-value is provided.\
            WARNING: note that, even though the b=0 volumes are never referred\
            to as shells in the literature, they still have to be explicitly\
            included in the list of b-values as provided to the -shell option!\
            Several algorithms which include the b=0 volumes in their\
            computations may otherwise return an undesired result.
        directions: specify the directions over which to apply the\
            non-negativity constraint (by default, the built-in 300 direction set\
            is used). These should be supplied as a text file containing [ az el ]\
            pairs for the directions.
        lmax: the maximum spherical harmonic order for the output FOD(s).For\
            algorithms with multiple outputs, this should be provided as a\
            comma-separated list of integers, one for each output image; for\
            single-output algorithms, only a single integer should be provided. If\
            omitted, the command will use the lmax of the corresponding response\
            function (i.e based on its number of coefficients), up to a maximum of\
            8.
        mask: only perform computation within the specified binary brain mask\
            image.
        filter_: the linear frequency filtering parameters used for the initial\
            linear spherical deconvolution step (default = [ 1 1 1 0 0 ]). These\
            should be supplied as a text file containing the filtering coefficients\
            for each even harmonic order.
        neg_lambda: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1).
        norm_lambda: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default = 1).
        threshold: the threshold below which the amplitude of the FOD is\
            assumed to be zero, expressed as an absolute amplitude (default = 0).
        niter: the maximum number of iterations to perform for each voxel\
            (default = 50). Use '-niter 0' for a linear unconstrained spherical\
            deconvolution.
        norm_lambda_1: the regularisation parameter lambda that controls the\
            strength of the constraint on the norm of the solution (default =\
            1e-10).
        neg_lambda_1: the regularisation parameter lambda that controls the\
            strength of the non-negativity constraint (default = 1e-10).
        predicted_signal: output the predicted dwi image.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dwi2fodOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWI2FOD_METADATA)
    params = dwi2fod_params(
        grad=grad,
        fslgrad=fslgrad,
        shells=shells,
        directions=directions,
        lmax=lmax,
        mask=mask,
        filter_=filter_,
        neg_lambda=neg_lambda,
        norm_lambda=norm_lambda,
        threshold=threshold,
        niter=niter,
        norm_lambda_1=norm_lambda_1,
        neg_lambda_1=neg_lambda_1,
        predicted_signal=predicted_signal,
        strides=strides,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        algorithm=algorithm,
        dwi=dwi,
        response_odf=response_odf,
    )
    return dwi2fod_execute(params, execution)


__all__ = [
    "DWI2FOD_METADATA",
    "Dwi2fodConfigParameters",
    "Dwi2fodFslgradParameters",
    "Dwi2fodOutputs",
    "Dwi2fodParameters",
    "Dwi2fodResponseOdfOutputs",
    "Dwi2fodResponseOdfParameters",
    "Dwi2fodVariousFileParameters",
    "Dwi2fodVariousStringParameters",
    "dwi2fod",
    "dwi2fod_config_params",
    "dwi2fod_fslgrad_params",
    "dwi2fod_params",
    "dwi2fod_response_odf_params",
    "dwi2fod_various_file_params",
    "dwi2fod_various_string_params",
]
